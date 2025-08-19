import java.math.BigDecimal;
import java.text.DecimalFormat;
import java.time.LocalDate;
import java.time.Period;
import java.time.format.DateTimeFormatter;
import java.util.*;

class Pessoa {
    private String nome;
    private LocalDate dataNascimento;

    public Pessoa(String nome, LocalDate dataNascimento) {
        this.nome = nome;
        this.dataNascimento = dataNascimento;
    }

    public String getNome() {
        return nome;
    }

    public LocalDate getDataNascimento() {
        return dataNascimento;
    }
}

class Funcionario extends Pessoa {
    private BigDecimal salario;
    private String funcao;

    public Funcionario(String nome, LocalDate dataNascimento, BigDecimal salario, String funcao) {
        super(nome, dataNascimento);
        this.salario = salario;
        this.funcao = funcao;
    }

    public BigDecimal getSalario() {
        return salario;
    }

    public String getFuncao() {
        return funcao;
    }

    public void aplicarAumento(BigDecimal percentual) {
        this.salario = this.salario.add(this.salario.multiply(percentual));
    }

    public BigDecimal qtdSalarios(BigDecimal salarioMinimo) {
        return this.salario.divide(salarioMinimo, 2, BigDecimal.ROUND_HALF_UP);
    }
}

public class Main {
    private static final DateTimeFormatter df = DateTimeFormatter.ofPattern("dd/MM/yyyy");
    private static final DecimalFormat dfNum = new DecimalFormat("#,##0.00");
    private static final BigDecimal SALARIO_MINIMO = new BigDecimal("1518.00");

    public static void main(String[] args) {
        List<Funcionario> funcionarios = new ArrayList<>();
        funcionarios.add(new Funcionario("Maria", LocalDate.of(2000, 10, 18), new BigDecimal("2009.44"), "Operador"));
        funcionarios.add(new Funcionario("João", LocalDate.of(1990, 5, 12), new BigDecimal("2284.38"), "Operador"));
        funcionarios.add(new Funcionario("Caio", LocalDate.of(1961, 5, 2), new BigDecimal("9836.14"), "Coordenador"));
        funcionarios.add(new Funcionario("Miguel", LocalDate.of(1988, 10, 14), new BigDecimal("19119.88"), "Diretor"));
        funcionarios.add(new Funcionario("Alice", LocalDate.of(1995, 1, 5), new BigDecimal("2234.68"), "Recepcionista"));
        funcionarios.add(new Funcionario("Heitor", LocalDate.of(1999, 11, 19), new BigDecimal("1582.72"), "Operador"));
        funcionarios.add(new Funcionario("Arthur", LocalDate.of(1993, 3, 31), new BigDecimal("4071.84"), "Contador"));
        funcionarios.add(new Funcionario("Laura", LocalDate.of(1994, 7, 8), new BigDecimal("3017.45"), "Gerente"));
        funcionarios.add(new Funcionario("Heloísa", LocalDate.of(2003, 5, 24), new BigDecimal("1606.85"), "Eletricista"));
        funcionarios.add(new Funcionario("Helena", LocalDate.of(1996, 9, 2), new BigDecimal("2799.93"), "Gerente"));

        System.out.println("--- Lista inicial ---");
        imprimirFuncionarios(funcionarios);

        // 3.2 remover João
        System.out.println("\nRemovendo João...");
        for (Iterator<Funcionario> it = funcionarios.iterator(); it.hasNext();) {
            if (it.next().getNome().equals("João")) {
                it.remove();
            }
        }

        // 3.3 imprimir todos os funcionários
        System.out.println("\nLista atualizada:");
        imprimirFuncionarios(funcionarios);

        // 3.4 aumento de 10%
        System.out.println("\nAplicando aumento de 10%...");
        for (Funcionario f : funcionarios) {
            f.aplicarAumento(new BigDecimal("0.10"));
        }
        imprimirFuncionarios(funcionarios);

        // 3.5 agrupar por função (versão mais simples)
        System.out.println("\nFuncionários agrupados por função:");
        Map<String, List<Funcionario>> porFuncao = new HashMap<>();
        for (Funcionario f : funcionarios) {
            porFuncao.computeIfAbsent(f.getFuncao(), k -> new ArrayList<>()).add(f);
        }
        for (String funcao : porFuncao.keySet()) {
            System.out.println("Função: " + funcao);
            imprimirFuncionarios(porFuncao.get(funcao));
        }

        // 3.8 aniversários nos meses 10 e 12
        System.out.println("\nAniversariantes de outubro e dezembro:");
        for (Funcionario f : funcionarios) {
            int mes = f.getDataNascimento().getMonthValue();
            if (mes == 10 || mes == 12) {
                System.out.println(f.getNome() + " - " + f.getDataNascimento().format(df));
            }
        }

        // 3.9 funcionário mais velho
        Funcionario maisVelho = funcionarios.get(0);
        for (Funcionario f : funcionarios) {
            if (f.getDataNascimento().isBefore(maisVelho.getDataNascimento())) {
                maisVelho = f;
            }
        }
        int idade = Period.between(maisVelho.getDataNascimento(), LocalDate.now()).getYears();
        System.out.println("\nFuncionário mais velho: " + maisVelho.getNome() + " (" + idade + " anos)");

        // 3.10 ordem alfabética
        System.out.println("\nFuncionários em ordem alfabética:");
        funcionarios.sort(Comparator.comparing(Funcionario::getNome));
        for (Funcionario f : funcionarios) {
            System.out.println(f.getNome());
        }

        // 3.11 soma dos salários
        BigDecimal total = BigDecimal.ZERO;
        for (Funcionario f : funcionarios) {
            total = total.add(f.getSalario());
        }
        System.out.println("\nSoma dos salários: " + dfNum.format(total));

        // 3.12 salários mínimos
        System.out.println("\nQuantos salários mínimos cada um recebe:");
        for (Funcionario f : funcionarios) {
            System.out.println(f.getNome() + " - " + f.qtdSalarios(SALARIO_MINIMO) + " salários mínimos");
        }
    }

    private static void imprimirFuncionarios(List<Funcionario> funcionarios) {
        for (Funcionario f : funcionarios) {
            System.out.println("Nome: " + f.getNome()
                    + " | Nascimento: " + f.getDataNascimento().format(df)
                    + " | Salário: " + dfNum.format(f.getSalario())
                    + " | Função: " + f.getFuncao());
        }
    }
}
