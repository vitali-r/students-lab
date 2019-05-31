from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TestProductsSample(APITestCase):

    @classmethod
    def setUpTestData(cls):  # noqa
        cls.products_url = reverse('api:products-list')
        cls.product_detail_url = reverse('api:products-detail', args=[1])  # 1 is potential ID

    def test__get_products_list__success(self):
        response = self.client.get(self.products_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test__get_product_detail__not_found(self):
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
