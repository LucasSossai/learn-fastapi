import json
from datetime import datetime


def test_create_job(client):
    data = {
        'title': 'Job Opening Test',
        'location': 'Brazil',
        'company': 'Ashley Testing',
        'description': 'Company created for test',
    }
    response = client.post('/jobs/create-job', json.dumps(data))
    assert response.status_code == 200
    assert response.json()['title'] == 'Job Opening Test'
    assert response.json()['location'] == 'Brazil'
    assert response.json()['company'] == 'Ashley Testing'
    assert response.json()['company_url'] is None
    assert response.json()['description'] == 'Company created for test'
    assert response.json()['date_posted'] == str(datetime.now().date())


def test_retrieve_job_by_id(client):
    data = {
        'title': 'Job Opening Test',
        'location': 'Brazil',
        'company': 'Ashley Testing',
        'description': 'Company created for test',
    }
    client.post('/jobs/create-job', json.dumps(data))
    response = client.get('/jobs/get/1')
    assert response.status_code == 200
    assert response.json()['title'] == 'Job Opening Test'
    assert response.json()['location'] == 'Brazil'
    assert response.json()['company'] == 'Ashley Testing'
    assert response.json()['company_url'] is None
    assert response.json()['description'] == 'Company created for test'
    assert response.json()['date_posted'] == str(datetime.now().date())
