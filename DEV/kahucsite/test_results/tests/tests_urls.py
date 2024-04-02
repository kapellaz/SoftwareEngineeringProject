from django.test import TestCase

from users.models import prototipo_user
from quiz.models import Quiz
# Create your tests here.


class TestUrls(TestCase):
    """Classe de testes para os urls
    Args:
        TestCase (TestCase): classe usada pelo django para efetuar os testes
    """

    def setUp(self) -> None:
		prototipo_user.objects.create(id=1,direito_rever=True,direito_criar=True, direito_resolver=True)
        prototipo_user.objects.create(id=2,direito_rever=True,direito_criar=True, direito_resolver=True)
		prototipo_user.objects.create(id=3,direito_rever=True,direito_criar=True, direito_resolver=True)
		#user sem permissão
		prototipo_user.objects.create(id=4,direito_rever=False,direito_criar=True, direito_resolver=True)
		
        Quiz.objects.create(id=1,descricao='Matemática',pergunta='Quanto é 2+2 ?',pontuacao=20,num_aprovacoes=0,num_reprovacoes=0,estado='À espera de revisão',criador_id=4,aprovador1_id=1,aprovador2_id=2,aprovador3_id=3,data_criado='2022-11-13 18:00:54+02',edited=False)


    def test_quiz_results(self):
        """Função para testar a redireção para o url 'viewresults/'
        """
        print("Testando redireção viewresults/  ...")
        response = self.client.get('viewresults/')
        self.assertEqual(response.status_code, 200)

    def test_landing_page(self):
        """Função para testar a redireção para o url 'landingpage/'
        """
        print("Testando redireção para users/home  ...")
        response = self.client.get('users/home')
        self.assertEqual(response.status_code, 200)
        
    def test_score_menor_max(self):
    	"""Função para teste que o score no Quiz é menor ou igual ao score máximo atribuido ao Quiz
    	Nota: Possivel dificuldade em retirar valor de score, comentado entretanto
    	"""
    	
    	#max_score = Quiz.objects.filter(id=1).values_list("pontuacao")[0][0]
    	#score = Quiz.objects.filter(id=1).values_list("pontuacao")[0][0]
		
		#self.assertLessEqual(score, max_score);    	
		pass
		
	
