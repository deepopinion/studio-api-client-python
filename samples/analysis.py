"""
Code Sample for downloading Batch Analysis of a Project
in table format and using pagination
to control the load on the server
"""
import csv
import os
from argparse import ArgumentParser

import requests


def get_project_analyses(
        workspace_id,
        project_id,
        api_token,
        offset=0,
        limit=25,
        details=None,
        host="https://api.deepopinion.ai"
):
    url = f"{host}/organizations/{workspace_id}/projects/{project_id}/analyses"
    params = {
        'offset': offset,
        'limit': limit,
        'details': details
    }
    headers = {
        'Authorization': f"Bearer {api_token}",
        'Content-Type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json(), response.elapsed.total_seconds()


def get_analysis_documents(
        workspace_id,
        analysis_id,
        api_token,
        offset=0,
        limit=100,
        details='segments,meta,tags'
):
    host = "https://api.deepopinion.ai"
    url = f"{host}/organizations/{workspace_id}/analyses/{analysis_id}/documents"

    params = {
        "offset": offset,
        "limit": limit,
        "details": details
    }
    headers = {
        'Authorization': f"Bearer {api_token}",
        'Content-Type': "application/json"
    }
    response = requests.request("GET", url, headers=headers, params=params)
    return response.json(), response.elapsed.total_seconds()


def flatten_documents(documents):
    """ Flatten documents object"""
    table = []
    for document in documents:
        segments = document.pop("segments", [])
        for segment in segments:
            tags = segment.pop("tags", [])
            for tag in tags:
                row = {k: v for k, v in document.items() if k not in ['segments']}
                row['segment_text'] = segment.get("text")
                row['span_start'] = segment["span"][0]
                row['span_end'] = segment["span"][1]
                row['class'] = tag.get("class")
                row['label'] = tag.get("label")
                table.append(row)
            if len(tags) == 0:
                row = {k: v for k, v in document.items() if k not in ['segments']}
                row['segment_text'] = segment.get("text")
                row['span_start'] = segment["span"][0]
                row['span_end'] = segment["span"][1]
                row['class'] = 'NONE'
                row['label'] = 'NONE'
                table.append(row)
    return table


def save_table_csv(table, fn):
    header = list(table[0].keys())
    with open(fn, 'w') as f:
        csvwriter = csv.writer(f, delimiter=',', quotechar='"')
        csvwriter.writerow(header)
        for row_dict in table:
            row = [row_dict.get(key) for key in header]
            csvwriter.writerow(row)


if __name__ == '__main__':
    api_token = os.getenv('STUDIO_API_TOKEN')  # for example eyJ0eXAiOiJKV1QiLCJh********************
    parser = ArgumentParser()
    parser.add_argument('-w', '--workspace_id', type=int, required=True, help='organization_id')
    parser.add_argument('-p', '--project_id', type=int, required=True, help='project_id')
    args = parser.parse_args()

    workspace_id = args.workspace_id
    project_id = args.project_id

    response_json, timedelta = get_project_analyses(workspace_id, project_id, api_token)
    print(f'Time elapsed for request analysis/project {project_id}: {timedelta} sec')

    for analysis in response_json['analyses']:
        print(analysis['id'], analysis['name'], analysis['created'], '#docs', analysis['document_count'])
        analysis_id = analysis['id']
        document_count = analysis['document_count']
        # looping over 50 documents each to keep requests small
        table_docs_of_analysis = []
        limit = 50
        for offset in range(0, document_count, limit):
            response_analysis_json, timedelta_analysis = get_analysis_documents(workspace_id, analysis_id, api_token,
                                                                                offset=offset, limit=limit)
            print(f'\toffset {offset}, Time elapsed for analysis {analysis_id}'
                  f' #docs {len(response_analysis_json["documents"])}: {timedelta} sec')
            table_docs_of_analysis.extend(flatten_documents(response_analysis_json["documents"]))

        # Do stuff with table ...
        # print(table_docs_of_analysis, '\n\n')
        save_table_csv(table_docs_of_analysis, f'{analysis["name"]}.csv')
