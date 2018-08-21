-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: Prefeitura
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu0.17.10.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Empenho`
--

DROP TABLE IF EXISTS `Empenho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Empenho` (
  `Especie` varchar(25) NOT NULL,
  `Orgao` varchar(100) NOT NULL,
  `Projeto` varchar(100) NOT NULL,
  `Elemento` varchar(100) NOT NULL,
  `Licitacao` varchar(50) NOT NULL,
  `Processo` varchar(30) NOT NULL,
  `DataEmpenho` date NOT NULL,
  `Valor` float NOT NULL,
  `Empenho_Numero` int(11) NOT NULL,
  `IdFavorecido` int(11) DEFAULT NULL,
  `Funcao` varchar(100) NOT NULL,
  `SubFuncao` varchar(100) NOT NULL,
  `Programa` varchar(100) NOT NULL,
  `Destinacao` varchar(45) NOT NULL,
  `idCliente` int(11) DEFAULT NULL,
  PRIMARY KEY (`Empenho_Numero`),
  KEY `fk_Empenho_Favorecido1_idx` (`IdFavorecido`),
  CONSTRAINT `fk_Empenho_Favorecido1` FOREIGN KEY (`IdFavorecido`) REFERENCES `Favorecido` (`IdFavorecido`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empenho`
--

LOCK TABLES `Empenho` WRITE;
/*!40000 ALTER TABLE `Empenho` DISABLE KEYS */;
INSERT INTO `Empenho` VALUES ('Estimativo','0209 - Fundo Municipal De Saude','2.104 - Manutencao De Convenio Com O Cispara','3.1.71.70.00 - Rateio Pela Participacao Em Consorcio Publico','0 - -','','2017-08-14',24462.4,7523,1,' 10 - Saude',' 302 - Assistencia Hospitalar E Ambulatorial',' 0022 - Atencao A Saude Da Comunidade',' 102 - Saude - 15%',NULL),('Global','0209 - Fundo Municipal De Saude','2.198 - Manutencao Cons. Urg/Emerg. Regiao Oeste Minas','3.1.71.70.00 - Rateio Pela Participacao Em Consorcio Publico','417 - 2017 - Processo De Dispensa',' PRC0066017','2017-09-14',136600,8676,2,' 10 - Saude',' 302 - Assistencia Hospitalar E Ambulatorial',' 0022 - Atencao A Saude Da Comunidade',' 102 - Saude - 15%',NULL),('Global','0209 - Fundo Municipal De Saude','2.359 - Manutencao Do Consorcio Com I.Cismep','3.1.71.70.00 - Rateio Pela Participacao Em Consorcio Publico','1417 - 2017 - Processo De Dispensa',' PRC0123417','2017-10-17',46093.8,9594,3,' 10 - Saude',' 302 - Assistencia Hospitalar E Ambulatorial',' 0022 - Atencao A Saude Da Comunidade',' 102 - Saude - 15%',NULL);
/*!40000 ALTER TABLE `Empenho` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-20 22:05:26
