from currency.models import Source


def test_get_api_rate_list(api_client):
    response = api_client.get('/v1/api/currency/rates/')
    assert response.status_code == 200


def test_post_api_rate_list(api_client):
    response = api_client.post('/v1/api/currency/rates/')
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'source': ['This field is required.']
    }


def test_get_api_source_list(api_client):
    response = api_client.get('/v1/api/currency/sources/')
    assert response.status_code == 200


def test_post_api_source_list(api_client):
    response = api_client.post('/v1/api/currency/sources/')
    assert response.status_code == 400
    assert response.json() == {
        'name': ['This field is required.'],
        'code_name': ['This field is required.'],
        'source_url': ['This field is required.']
    }


def test_post_api_source_create(api_client):
    data = {
        'name': 'test',
        'code_name': 'test',
        'source_url': 'test'
    }
    response = api_client.post('/v1/api/currency/sources/', data=data)
    assert response.status_code == 201
    assert Source.objects.filter(name='test', code_name='test', source_url='test').exists()


def test_post_api_source_update(api_client):
    obj = Source.objects.latest('id')
    pk = obj.pk
    data = {
        'name': 'test2',
        'code_name': 'test2',
        'source_url': 'test2'
    }
    response = api_client.put(f'/v1/api/currency/sources/{pk}/', data=data)
    assert response.status_code == 200
    assert response.json() == {
        'id': pk,
        'name': 'test2',
        'code_name': 'test2',
        'source_url': 'test2',
        'phone': 'asas',
        'email': 'oleksandr.ostrolutsky@gmail.com'
    }


def test_post_api_source_delete(api_client):
    obj = Source.objects.latest('id')
    pk = obj.pk
    response = api_client.delete(f'/v1/api/currency/sources/{pk}/')
    assert response.status_code == 204
    assert not Source.objects.filter(pk=pk).exists()
