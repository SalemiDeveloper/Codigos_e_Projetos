<?php
defined('CONTROL') or die('Acesso negado!');
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Aplicação</title>
</head>
<body>
    <h3>Bem vindo à Aplicação</h3>
    <hr>
    <span>Usuário: <strong><?php echo $_SESSION['usuario']; ?></strong></span>
    <span>
        <a href="?rota=logout">Sair</a>
        <hr>
        [conteúdo]
    </span>
</body>
</html>