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
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`IdFavorecido`,`idCliente`),
  UNIQUE KEY `Nome_UNIQUE` (`Nome`),
  UNIQUE KEY `IdFavorecido_UNIQUE` (`IdFavorecido`),
  KEY `fk_Favorecido_1_idx` (`idCliente`),
  CONSTRAINT `fk_Favorecido_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`) ON DELETE NO ACTION ON UPDATE NO ACTION
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
  `Empenho_Numero` int(11) DEFAULT NULL,
  `idCliente` int(11) NOT NULL,
  PRIMARY KEY (`Numero`,`idCliente`),
  KEY `fk_Pagamento_1_idx` (`idCliente`),
  CONSTRAINT `fk_Pagamento_1` FOREIGN KEY (`idCliente`) REFERENCES `Cliente` (`idCliente`) ON DELETE NO ACTION ON UPDATE NO ACTION
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

-- Dump completed on 2018-08-28  9:08:17
