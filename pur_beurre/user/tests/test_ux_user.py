# coding=utf-8
import os
import pytest
from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

BASE_DIR = \
    os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep)[:-2])
os.environ["PATH"] += os.pathsep + os.path.join(BASE_DIR, 'driver')

@pytest.mark.skipif('DEPLOY_ENVIRON' in os.environ and os.environ['DEPLOY_ENVIRON'] == 'PRODUCTION',
                    reason="requires production environement")
class AccountTestCase(LiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_login_success(self):
        """
        Test fonctionnel de création d'un user
        :return:
        """
        self.sub_register_success()
        self.sub_login_success()
        self.sub_register_fail_yet_registered()
        self.sub_register_clean()


    def sub_register_clean(self):
        """  supprime un user
        précedemment créé pour les tests"""
        pass

    def sub_register_success(self):
        """  crée un user pour le test """
        time.sleep(10)
        self.driver.get(self.live_server_url + '/user/register/')
        time.sleep(10)

        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Jose')
        self.driver.implicitly_wait(5)

        password1 = self.driver.find_element_by_id('id_password1')
        password1.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        email = self.driver.find_element_by_id('id_email')
        email.send_keys('Jose@dummies.com')
        self.driver.implicitly_wait(5)

        password2 = self.driver.find_element_by_id('id_password2')
        password2.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and contains(text(), 'Créer le compte')]")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
               WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((((By.XPATH, "//h2[contains(text(), 'Hello')]")))))
        except:
            assert(1 == 0)


    def sub_register_fail_yet_registered(self):
        """  crée un user existant pour le test
        on ne vérifie juste que le msg d'erreur
        concernant l'adresse mail deja utilisée """

        # dans le doute on clique sur deconnexion
        try:
            dconx = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//a[contains(text(), 'DECONNEXION')]")))))
            dconx.click()
        except:
            self.assertIsNotNone(dconx)



        time.sleep(10)
        self.driver.get(self.live_server_url + '/user/register/')
        time.sleep(10)

        username = self.driver.find_element_by_id('id_username')
        username.clear()
        username.send_keys('Jose')
        self.driver.implicitly_wait(5)

        password1 = self.driver.find_element_by_id('id_password1')
        password1.clear()
        password1.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        email = self.driver.find_element_by_id('id_email')
        email.clear()
        email.send_keys('Jose@dummies.com')
        self.driver.implicitly_wait(5)

        password2 = self.driver.find_element_by_id('id_password2')
        password2.clear()
        password2.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and contains(text(), 'Créer le compte')]")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
            test = WebDriverWait(self.driver, 100).until(
                EC.presence_of_element_located((((By.XPATH, "//p[contains(@class, 'text-info') and contains(text(), '[Un utilisateur avec ce nom existe déjà.]')]")))))
        except:
            assert(1 == 0)



    def sub_login_success(self):
        """ doit réussir si le user a été créée """
        time.sleep(10)
        self.driver.get(self.live_server_url + '/user/login/')
        time.sleep(10)

        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Jose@dummies.com')
        self.driver.implicitly_wait(5)

        password = self.driver.find_element_by_id('id_password')
        password.send_keys('J053_1234')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and text()='Login']")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
              WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//h2[contains(text(), 'Hello')]")))))
        except:
            assert(1 == 0)



    def test_login_fail(self):
        """
        User does not exist
        err msg should appear
        """
        time.sleep(10)
        self.driver.get(self.live_server_url + '/user/login/')
        time.sleep(10)

        username = self.driver.find_element_by_id('id_username')
        username.send_keys('Sejo')
        self.driver.implicitly_wait(5)

        password = self.driver.find_element_by_id('id_password')
        password.send_keys('false_pwd')
        self.driver.implicitly_wait(5)

        try:
            submit = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//button[@type='submit' and text()='Login']")))))
            submit.click()
        except:
            self.assertIsNotNone(submit)

        try:
             WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((((By.XPATH, "//p[contains(@class, 'danger') and contains(text(), 'Veuillez saisir à nouveau vos identifiants ou créer un compte')]")))))
        except:
            assert(1 == 0)

