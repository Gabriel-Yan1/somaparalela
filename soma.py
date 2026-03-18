import multiprocessing
import time
import os

def somar_bloco(sublista):
    """Esta funcao roda em cada nucleo separadamente."""
    return sum(sublista)

def processar_arquivo():
    # 1. Localizacao do arquivo
    arquivo_nome = 'numero2.txt'
    
    if not os.path.exists(arquivo_nome):
        print(f"Erro: O arquivo '{arquivo_nome}' nao foi encontrado na pasta atual.")
        return

    # 2. Leitura dos dados
    print(f"Lendo dados de {arquivo_nome}...")
    try:
        with open(arquivo_nome, 'r', encoding='utf-8') as f:
            # Converte cada linha para inteiro
            numeros = [int(linha.strip()) for linha in f if linha.strip()]
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return
    
    total_elementos = len(numeros)
    print(f"Sucesso: {total_elementos} numeros carregados.")

    # 3. Definicao da quantidade de nucleos
    cores_max = multiprocessing.cpu_count()
    print(f"\nSeu PC possui {cores_max} nucleos disponiveis.")
    
    try:
        entrada = input(f"Quantos nucleos quer usar? (1-{cores_max}): ")
        n_cores = int(entrada)
        if n_cores < 1 or n_cores > cores_max:
            print(f"Valor fora do limite. Usando {cores_max} nucleos.")
            n_cores = cores_max
    except ValueError:
        print("Entrada invalida. Usando 1 nucleo.")
        n_cores = 1

    # 4. Divisao da carga de trabalho
    tamanho_chunk = max(1, total_elementos // n_cores)
    chunks = [numeros[i:i + tamanho_chunk] for i in range(0, total_elementos, tamanho_chunk)]

    # 5. Execucao em Paralelo
    print(f"Iniciando soma paralela com {n_cores} nucleo(s)...")
    inicio = time.time()

    with multiprocessing.Pool(processes=n_cores) as pool:
        resultados_parciais = pool.map(somar_bloco, chunks)

    soma_final = sum(resultados_parciais)
    fim = time.time()

    # 6. Exibicao do Resultado
    print("\n" + "="*40)
    print(f"RESULTADO DA SOMA: {soma_final}")
    print(f"TEMPO TOTAL: {fim - inicio:.6f} segundos")
    print(f"NUCLEOS UTILIZADOS: {n_cores}")
    print("="*40)

if __name__ == "__main__":
    processar_arquivo()