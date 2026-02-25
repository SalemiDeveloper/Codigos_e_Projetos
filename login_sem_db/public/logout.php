<?php
defined('CONTROL') or die('Acesso negado!');

// Efetuando o logout
session_destroy();

// Voltando para a página inicial
header('Location: index.php?rota=login');