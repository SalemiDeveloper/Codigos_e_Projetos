<?php
// CONTINUAR VÍDEO 41:56


// Iniciando a sessão
session_start();

// Definindo uma constante de controle
define('CONTROL', true);

// Verificando se existe usuário logado
$usuario_logado = $_SESSION['usuario'] ?? null; // esse "??" irá retornar null caso $_SESSION['usuario'] não exista.

// Verificando qual a rota na URL
if (empty($usuario_logado)) { 
    $rota = 'login';
} else {
    $rota = $_GET['rota'] ?? 'home';
}

// Verificando se o usuário já está logado, mas a rota é 'login'. Vai redirecionar para 'home'
if (!empty($usuario_logado) && $rota == 'login') {
    $rota = 'home';
}

// Analisando a rota
$rotas = [
    'login'  => 'login.php',
    'home'   => 'home.php',
    'logout' => 'logout.php'
];

// Verificando se $rota existe em $rotas
if (!key_exists($rota, $rotas)) {
    die('Acesso negado!');
}

require_once $rotas[$rota];