<?php

defined('CONTROL') or die('Acesso negado!');

// Verificando se o formulário foi submetido.
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    
    // Verificando se o usuário e a senha foram submetidos.
    $usuario = $_POST['usuario'] ?? null;
    $senha   = $_POST['senha']   ?? null;
    $erro = null;

    if (empty($usuario) || empty($senha)) {
        $erro = 'Usuário e senha são obrigatórios!';
    }

    // Verificando se o usuário e senha são válidos.
    if (empty($erro)) {
        $usuarios = require_once __DIR__ . '/../inc/usuarios.php';

        foreach ($usuarios as $user) {

            if ($user['usuario'] == $usuario && password_verify($senha, $user['senha'])) {

                // Efetuando o login
                $_SESSION['usuario'] = $usuario;

                // Voltando a página inicial
                header('Location: index.php?rota=home');
            }
        }

        // Login inválido
        $erro = "Usuário e/ou senha inválidos!";
    }
}
?>

<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>login</title>
</head>
<body>
    
    <form action="index.php?rota=login" method="POST">
        <h3>Login</h3>
        <div>
            <label for="usuario">Usuário</label>
            <input type="email" name="usuario" id="usuario">
        </div>
        <div>
            <label for="senha">Senha</label>
            <input type="password" name="senha" id="senha">
        </div>
        <div>
            <button type="submit">Entrar</button>
        </div>
    </form>

    <?php if (!empty($erro)) : ?>
        <p style="color:red"><?php echo $erro ?></p>
    <?php endif; ?>

</body>
</html>