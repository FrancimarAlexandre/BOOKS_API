// Pode adicionar validações ou outras interações
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Previne o envio do formulário
    // Implemente a lógica de login
    alert('Login efetuado com sucesso!');
});

document.getElementById('registerForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Previne o envio do formulário
    // Implemente a lógica de cadastro
    const password = document.getElementById('newPassword').value;
    const confirmPassword = document.getElementById('confirmPassword').value;

    if(password === confirmPassword) {
        alert('Cadastro efetuado com sucesso!');
        // Aqui você pode adicionar a lógica para realmente registrar o usuário
    } else {
        alert('As senhas não coincidem.');
    }
});
