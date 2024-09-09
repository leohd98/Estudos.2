alert('Boas vindas ao jogo do número secreto');
let numerodecasas = 100;
let numeroSecreto = parseInt(Math.random() * numerodecasas + 1);
let numeroEscolhido
let tentativas = 1;

while (numeroEscolhido != numeroSecreto) {
    
    numeroEscolhido = prompt(`Escolha um número entre 1 e ${numerodecasas}`);

    if (numeroEscolhido > numeroSecreto) {
        alert(`O número secreto é menor que ${numeroEscolhido}`);
        tentativas++
    } else if (numeroEscolhido < numeroSecreto) {
        alert(`O número secreto é maior que ${numeroEscolhido}`);
        tentativas++
    } else {
        break;
    }
}

let palavraTentativa = tentativas > 1 ? 'tentativas' : 'tentativa';
alert(`Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`);