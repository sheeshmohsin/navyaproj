import json
from django.test import TestCase

# Create your tests here.

class UserPermissionTest(TestCase):
    fixtures = ['dump.json']

    def test_status_code_1(self):
        # Testing GET request
        resp = self.client.get('/user/user1/')
        self.assertEqual(resp.status_code, 200)

    def test_status_code_2(self):
        # Testing GET request
        resp = self.client.get('/user/user5/')
        self.assertEqual(resp.status_code, 404)

    def test_data(self):
        data = ["perm1", "perm7", "perm6", "perm5"]
        resp = self.client.get('/user/user1/')
        self.assertListEqual(data, json.loads(resp.content))

    def test_other_method(self):
        resp = self.client.post('/user/user1/')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.put('/user/user1/')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.delete('/user/user1/')
        self.assertEqual(resp.status_code, 405)


class PermissionCheckTest(TestCase):
    fixtures = ['dump.json']

    def test_status_code_1(self):
        resp = self.client.get('/checkpermission/?userid=user1&permissionid=perm1')
        self.assertEqual(resp.status_code, 200)

    def test_status_code_2(self):
        resp = self.client.get('/checkpermission/?userid=user1&permissionid=perm2')
        self.assertEqual(resp.status_code, 404)

    def test_status_code_3(self):
        resp = self.client.get('/checkpermission/?userid=user2&permissionid=perm2')
        self.assertEqual(resp.status_code, 404)

    def test_data(self):
        resp = self.client.get('/checkpermission/?userid=user1&permissionid=perm1')
        self.assertEqual(resp.content, json.dumps(True))

    def test_other_method(self):
        resp = self.client.post('/checkpermission/?userid=user1&permissionid=perm1')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.put('/checkpermission/?userid=user1&permissionid=perm1')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.delete('/checkpermission/?userid=user1&permissionid=perm1')
        self.assertEqual(resp.status_code, 405)

        
class PermissionDeleteTest(TestCase):
    fixtures = ['dump.json']

    def test_status_code_1(self):
        resp = self.client.delete('/permissions/perm1/')
        self.assertEqual(resp.status_code, 200)

    def test_status_code_2(self):
        resp = self.client.delete('/permissions/perm9/')
        self.assertEqual(resp.status_code, 404)

    def test_data(self):
        resp = self.client.delete('/permissions/perm5/')
        self.assertEqual(resp.content, "ok")

    def test_other_method(self):
        resp = self.client.post('/permissions/perm1/')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.put('/permissions/perm1/')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.get('/permissions/perm1/')
        self.assertEqual(resp.status_code, 405)


class ModifyPermisionTest(TestCase):
    fixtures = ['dump.json']

    def test_status_code_1(self):
        resp = self.client.post('/roles/role1/', 
                                json.dumps({"permissions": ["perm1", "perm5"]}),
                                content_type="application/json")
        self.assertEqual(resp.status_code, 200)

    def test_status_code_2(self):
        resp = self.client.post('/roles/role1/', 
                                json.dumps({"permissions": ["perm1", "perm9"]}),
                                content_type="application/json")
        self.assertEqual(resp.status_code, 404)

    def test_status_code_3(self):
        resp = self.client.post('/roles/role8/', 
                                json.dumps({"permissions": ["perm1", "perm9"]}),
                                content_type="application/json")
        self.assertEqual(resp.status_code, 404)

    def test_data(self):
        resp = self.client.post('/roles/role1/', 
                                json.dumps({"permissions": ["perm1", "perm5"]}),
                                content_type="application/json")
        self.assertEqual(resp.content, "Ok")

    def test_other_method(self):
        resp = self.client.delete('/roles/role1/')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.put('/roles/role1/')
        self.assertEqual(resp.status_code, 405)
        resp = self.client.get('/roles/role1/')
        self.assertEqual(resp.status_code, 405)


