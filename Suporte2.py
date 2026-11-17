def analisar_pedidos(): 
    # Inicializar variáveis conforme o fluxograma 
    i = 1 
    urgentes = 0 
    total_minutos = 0 
    maior_tempo = 0

    NUMERO_PEDIDOS = 10
 
    print("=== ANÁLISE DE PEDIDOS DE SUPORTE ===") 
 
    # Contador i <= NUMERO_PEDIDOS? 
    while i <= NUMERO_PEDIDOS: 
        print(f"\n--- Pedido #{i} ---") 
         
        # Ler prioridade, tempo 
        try: 
            prioridade = int(input("Introduza a prioridade (1 a 5): ")) 
            tempo = int(input("Introduza o tempo estimado (minutos): ")) 
        except ValueError: 
            prioridade = -1 
            tempo = -1 
 
        # Validação: (1 <= prioridade <= 5) E (tempo > 0)? 
        if 1 <= prioridade <= 5 and tempo > 0: 
            # Manter valor 
            pass 
        else: 
            # Atribuir por omissão 
            print("Dados inválidos! A assumir valores por omissão: Prioridade = 5, Tempo = 20.") 
            prioridade = 5 
            tempo = 20 
 
        # Processar Valores do Pedido 
        if prioridade <= 2: 
            urgentes += 1 
             
        total_minutos = total_minutos + tempo 
         
        if tempo > maior_tempo: 
            maior_tempo = tempo 
             
        i = i + 1 
 
    # Calcular média: total_minutos / NUMERO_PEDIDOS 
    media = total_minutos / NUMERO_PEDIDOS 
 
    # Classificar Carga 
    if total_minutos <= 300: 
        classificacao = "Carga Baixa" 
    else: 
        if total_minutos <= 400: 
            classificacao = "Carga Moderada" 
        else: 
            classificacao = "Carga Elevada" 
 
    # Apresentar Resultados Finais 
    print("\n==========================================") 
    print("APRESENTAR RESULTADOS FINAIS:") 
    print(f"- Nº de urgentes: {urgentes}") 
    print(f"- Total de minutos: {total_minutos}") 
    print(f"- Média por pedido: {media:.1f}") 
    print(f"- Maior estimativa: {maior_tempo}") 
    print(f"- Classificação: {classificacao}") 
    print("==========================================") 
 
# Executar a função 
analisar_pedidos() 