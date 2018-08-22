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
-- Table structure for table `Cliente`
--

DROP TABLE IF EXISTS `Cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Cliente` (
  `idCliente` int(11) NOT NULL,
  `nome` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`idCliente`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Cliente`
--

LOCK TABLES `Cliente` WRITE;
/*!40000 ALTER TABLE `Cliente` DISABLE KEYS */;
INSERT INTO `Cliente` VALUES (7,'Prefeitura Municipal de Aimorés'),(16,'Prefeitura Municipal de Argirita'),(20,'Prefeitura Municipal de Bandeira'),(21,'Prefeitura Municipal de Barão de Cocais'),(22,'Prefeitura Municipal de Bela Vista de Minas'),(23,'Prefeitura Municipal de Belo Oriente'),(26,'Prefeitura Municipal de Bom Jesus do Galho'),(33,'Câmara Municipal de Bandeira'),(35,'Câmara Municipal de Braúnas'),(40,'Câmara Municipal de Coronel Fabriciano'),(46,'Câmara Municipal de Itabira'),(47,'Câmara Municipal de Lagoa Santa'),(50,'Custom - Câmara Municipal de Nova Serrana'),(64,'Prefeitura Municipal de Caratinga'),(67,'Prefeitura Municipal de Catas Altas'),(72,'CISVI'),(78,'Prefeitura Municipal de Coronel Fabriciano'),(94,'Prefeitura Municipal de Governador Valadares'),(97,'Prefeitura Municipal de Ipatinga'),(106,'Prefeitura Municipal de Jordânia'),(115,'Prefeitura Municipal de Manhumirim'),(124,'Prefeitura Municipal de Nova Era'),(134,'Prefeitura Municipal de Peçanha'),(135,'Prefeitura de Periquito'),(147,'Prefeitura Municipal de Raul Soares'),(154,'Custom - SAAE de Aimorés'),(156,'SAAE de Itapemirim'),(162,'Prefeitura Municipal de Santa Bárbara'),(164,'Prefeitura Municipal de Santana do Paraíso'),(167,'Prefeitura Municipal de São Gonçalo do Rio Abaixo'),(175,'Prefeitura Municipal de Três Pontas'),(178,'Prefeitura Municipal de Ubá'),(186,'Prefeitura Municipal de São Francisco de Paula'),(194,'Câmara Municipal de Belo Oriente'),(201,'SAAE de Governador Valadares Transparência'),(205,'Câmara Municipal de Taubaté'),(210,'Demonstração'),(214,'IPREM Governador Valadares'),(215,'Prefeitura Municipal de Tapiraí'),(216,'Prefeitura Municipal de Carmo da Mata'),(217,'Câmara Municipal de Píuma'),(218,'Prefeitura Municipal de Tarumirim'),(220,'Prefeitura Municipal de Ilhéus'),(225,'Câmara Municipal de Biquinhas'),(230,'Consórcio Intermunicipal de Saúde do Vale do Rio Doce'),(235,'Câmara Municipal de Capim Branco'),(240,'Fundo Municipal de Saúde Ilhéus'),(242,'Prefeitura Municipal de São José do Ribamar'),(245,'Prefeitura Municipal de Pará de Minas'),(247,'Prefeitura Municipal de Fernandes Tourinho'),(253,'Prefeitura Municipal de Leopoldina'),(257,'Prefeitura Municipal de Santo Antônio do Jacinto'),(265,'Prefeitura Municipal de Ituaçu'),(269,'Prefeitura Municipal de São João do Oriente'),(271,'Prefeitura Municipal de Bicas'),(272,'Prefeitura Municipal de Itagiba'),(278,'Prefeitura Municipal de Viçosa'),(279,'SAAE de Manhumirim'),(280,'Prefeitura Municipal de Sarzedo'),(281,'Prefeitura Municipal de Paraopeba'),(284,'Prefeitura Municipal de Itaobim'),(286,'Prefeitura Municipal de Timóteo'),(287,'Prefeitura Municipal de Alto Rio Doce'),(288,'Prefeitura Municipal de Jaguaraçu'),(290,'Prefeitura Municipal de Presidente Jânio Quadros'),(291,'Fundação Hospitalar do Município de Varginha'),(292,'Câmara Municipal de Jaguaraçu'),(293,'Prefeitura Municipal de Senador Cortes'),(296,'Prefeitura Municipal de Durandé'),(299,'Prefeitura Municipal de Açucena'),(300,'Prefeitura Municipal de Alpinopolis'),(301,'Prefeitura Municipal de Naque'),(302,'Prefeitura Municipal de Machado'),(303,'Prefeitura Municipal de Japaraíba'),(305,'Câmara Municipal de Senador Cortes'),(306,'Prefeitura Municipal de Passos'),(307,'Prefeitura Municipal de Cássia'),(310,'Prefeitura Municipal de Bugre'),(312,'Demonstração Portal Fácil'),(315,'Prefeitura Municipal de Nova Ibiá'),(316,'Prefeitura Municipal de Mesquita'),(317,'MGS'),(318,'Prefeitura Municipal de Vermelho Novo'),(319,'Prefeitura Municipal de Piedade de Caratinga'),(320,'Prefeitura Municipal de Cajuri'),(321,'Prefeitura Municipal de Itagi'),(322,'Câmara Municipal de São Sebastião do Paraíso'),(326,'Prefeitura Municipal de Inhapim'),(327,'Câmara Municipal de Jerônimo Monteiro'),(328,'Prefeitura Municipal de Antônio Dias'),(329,'Prefeitura Municipal de Medina'),(330,'Prefeitura Municipal de Iapu'),(331,'Prefeitura Municipal de Pompeu'),(332,'Câmara Municipal de Antônio Dias'),(333,'Câmara Municipal de Ilhéus'),(335,'Prefeitura Municipal de São Domingos das Dores'),(336,'Câmara Municipal de Mimoso do Sul'),(338,'Prefeitura Municipal de Jequeri'),(339,'Prefeitura Municipal de Chiador'),(340,'Câmara Municipal de Capetinga'),(341,'Prefeitura Municipal de Dom Cavati'),(342,'Câmara Municipal de Congonhas'),(344,'Prefeitura Municipal de Joanésia'),(347,'Câmara Municipal de Itaobim'),(349,'Prefeitura Municipal de São Pedro de Ferros'),(350,'Prefeitura Municipal de Capetinga'),(351,'Prefeitura Municipal de Cambuí'),(352,'Prefeitura Municipal de Pratápolis'),(353,'Câmara Municipal de Alpinópolis'),(354,'Câmara Municipal de Simão Pereira'),(355,'Prefeitura Municipal de São Sebastião do Anta'),(356,'Prefeitura Municipal de Santa Barbará do Leste'),(357,'Prefeitura Municipal de Ipaba'),(358,'Câmara Municipal de Carmópolis de Minas'),(359,'Câmara Municipal de São João do Oriente'),(361,'Demonstração Portal da Transparência'),(362,'Câmara Municipal de Bugre'),(363,'Câmara Municipal de São Domingos das Dores'),(365,'Câmara Municipal de Pratápolis'),(366,'Prefeitura Municipal de Ponto dos Volantes'),(367,'Prefeitura Municipal de Conselheiro Pena'),(369,'Serviço Autônomo Municipal de Limpeza Urbana'),(370,'Câmara Municipal de Jequeri'),(371,'Câmara Municipal de São José do Divino'),(372,'Prefeitura Municipal de Imbé de Minas'),(373,'Prefeitura Municipal de Monte Formoso'),(374,'Prefeitura Municipal de Dionísio'),(375,'Câmara Municipal de Munhoz'),(378,'Prefeitura Municipal de Sete Lagoas'),(379,'Prefeitura Municipal de Padre Paraíso'),(380,'Câmara Municipal de Barão de Cocais'),(381,'Prefeitura Municipal de Maravilhas'),(382,'Prefeitura Municipal de Ubaporanga'),(386,'Câmara Municipal de Tiros'),(388,'Câmara Municipal de Conselheiro Pena'),(389,'Prefeitura Municipal de Pingo D Água'),(391,'Prefeitura Municipal de Dores do Rio Preto'),(393,'Câmara Municipal de Jordânia'),(394,'Prefeitura Municipal de Córrego Novo'),(395,'Câmara Municipal de Córrego Novo'),(396,'Custom - SAAE Baixo Guandu'),(399,'Prefeitura Municipal de Ribeirão das Neves'),(400,'Prefeitura Municipal de Aiquara'),(401,'Prefeitura Municipal de Nova Serrana'),(402,'Câmara Municipal de Orizânia'),(404,'Câmara Municipal de Santana do Paraíso'),(406,'Câmara Municipal de Durandé'),(407,'Câmara Municipal de Bela Vista de Minas'),(409,'Câmara Municipal de Sobrália'),(410,'Câmara Municipal de Naque'),(411,'Câmara Municipal de Taparuba'),(412,'Prefeitura Municipal de Santana de Cataguases'),(415,'Câmara Municipal de Alvarenga'),(416,'Câmara Municipal de Caratinga'),(418,'Prefeitura Municipal de Alvarenga'),(419,'Câmara Municipal de Santa Rita de Minas'),(420,'Câmara Municipal de Barbacena'),(422,'Prefeitura Municipal de Conceição de Ipanema'),(425,'Câmara Municipal de Monte Santo de Minas'),(427,'Prefeitura Municipal de Monte Santo de Minas'),(428,'Consórcio Intermunicipal Multissetorial do entorno do Caparaó'),(429,'Câmara Municipal de Pedra Azul'),(430,'Câmara Municipal de Jequitinhonha'),(431,'Prefeitura Municipal de Palma'),(432,'Prefeitura de Santa Maria de Itabira'),(435,'Câmara Municipal de Tarumirim');
/*!40000 ALTER TABLE `Cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Empenho`
--

DROP TABLE IF EXISTS `Empenho`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Empenho` (
  `Empenho_Numero` int(11) NOT NULL,
  `Especie` varchar(25) NOT NULL,
  `Orgao` varchar(100) NOT NULL,
  `Projeto` varchar(100) NOT NULL,
  `Elemento` varchar(100) NOT NULL,
  `Licitacao` varchar(50) NOT NULL,
  `Processo` varchar(30) NOT NULL,
  `DataEmpenho` date NOT NULL,
  `Valor` decimal(12,2) DEFAULT NULL,
  `IdFavorecido` int(11) NOT NULL,
  `Funcao` varchar(100) NOT NULL,
  `SubFuncao` varchar(100) NOT NULL,
  `Programa` varchar(100) NOT NULL,
  `Destinacao` varchar(45) NOT NULL,
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`Empenho_Numero`,`IdFavorecido`,`idCliente`),
  KEY `fk_Empenho_Favorecido1_idx` (`IdFavorecido`),
  KEY `fk_Empenho_Cliente1_idx` (`idCliente`),
  CONSTRAINT `fk_Empenho_Cliente1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`) ON DELETE NO ACTION ON UPDATE NO ACTION,
  CONSTRAINT `fk_Empenho_Favorecido1` FOREIGN KEY (`IdFavorecido`) REFERENCES `Favorecido` (`IdFavorecido`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Empenho`
--

LOCK TABLES `Empenho` WRITE;
/*!40000 ALTER TABLE `Empenho` DISABLE KEYS */;
/*!40000 ALTER TABLE `Empenho` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Favorecido`
--

DROP TABLE IF EXISTS `Favorecido`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Favorecido` (
  `IdFavorecido` int(11) NOT NULL AUTO_INCREMENT,
  `CPF_CNPJ` varchar(20) NOT NULL,
  `Nome` varchar(100) NOT NULL,
  `Cargo` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`IdFavorecido`),
  UNIQUE KEY `Nome_UNIQUE` (`Nome`),
  UNIQUE KEY `IdFavorecido_UNIQUE` (`IdFavorecido`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Favorecido`
--

LOCK TABLES `Favorecido` WRITE;
/*!40000 ALTER TABLE `Favorecido` DISABLE KEYS */;
/*!40000 ALTER TABLE `Favorecido` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Pagamento`
--

DROP TABLE IF EXISTS `Pagamento`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Pagamento` (
  `Numero` int(11) NOT NULL,
  `DataPagamento` date NOT NULL,
  `ValorPagamento` decimal(12,2) DEFAULT NULL,
  `Empenho_Numero` int(11) NOT NULL,
  PRIMARY KEY (`Numero`,`Empenho_Numero`),
  KEY `fk_Pagamento_Empenho1_idx` (`Empenho_Numero`),
  CONSTRAINT `fk_Pagamento_Empenho1` FOREIGN KEY (`Empenho_Numero`) REFERENCES `Empenho` (`Empenho_Numero`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Pagamento`
--

LOCK TABLES `Pagamento` WRITE;
/*!40000 ALTER TABLE `Pagamento` DISABLE KEYS */;
/*!40000 ALTER TABLE `Pagamento` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-08-22 17:28:03
