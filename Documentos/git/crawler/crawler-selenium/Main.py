__author__ = "Gustavo Almeida"
import ManipulaPrimeiraTabela
import dados


#link_elemento = "http://transparencia.parademinas.mg.gov.br/despesas-por-elementos"       #ok ok
#link_fornecedor = "http://transparencia.parademinas.mg.gov.br/despesas-por-fornecedores"  #ok ok
#link_unidade ="http://transparencia.parademinas.mg.gov.br/despesas-por-unidades"          #ok ok
#link_acao = "http://transparencia.parademinas.mg.gov.br/despesas-por-acoes"               #ok ok
#link_despesas_diarias = "http://transparencia.parademinas.mg.gov.br/despesas-por-diarias" #ok ok
link_despesas_diarias = "http://transparencia.parademinas.mg.gov.br/tpc_des_dia_lis.aspx?tipo=d&exercicio=2017&cdElemento=3.3.90.14"
link_despesas_elemento = "http://transparencia.parademinas.mg.gov.br/tpc_des_forn_lis.aspx?exercicio=2017&cdElemento=3.1.71.70.00&dsElemento=Rateio%20Pela%20Participacao%20Em%20Consorcio%20Publico"
#link_licitacoes = "http://transparencia.parademinas.mg.gov.br/despesas-por-licitacoes"    #ok OK
#link_extra = "http://transparencia.parademinas.mg.gov.br/despesas-extras?tipo=d"          #ok ok
#link_restos = "http://transparencia.parademinas.mg.gov.br/restos-a-pagar-por-fornecedores"#ok


c = ManipulaPrimeiraTabela.CapturaDados(link_despesas_elemento)
c.Inicia_Captura(0)
c.InserirDados()
