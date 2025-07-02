# app/services/mock_services.py

import re

def gerar_resposta(mensagem: str, contexto: list) -> str:
    """
    Função mock para simular respostas da NutriAI (OpenAI) com maior abrangência.
    """
    mensagem = mensagem.lower()  # Para facilitar a comparação

    # Utilizando expressões regulares para tentar encontrar padrões de perguntas

    # Respostas sobre dietas e nutrientes
    if re.search(r"(proteína|whey|leguminosa|carne|ovo)", mensagem):
        return "Uma dieta rica em proteínas pode incluir ovos, peixes, frango, carne magra, tofu e leguminosas como feijão e lentilhas."
    elif re.search(r"(carboidrato|açúcar|pão|massa|batata)", mensagem):
        return "Carboidratos são essenciais para fornecer energia ao corpo. Exemplos incluem arroz, batata, massas, pães integrais e quinoa."
    elif re.search(r"(gordura|lipídios|azeite|oleaginosas|abacate)", mensagem):
        return "As gorduras saudáveis são importantes para a absorção de vitaminas. Exemplos incluem abacate, azeite de oliva, oleaginosas e peixes como salmão."
    elif re.search(r"(vitamina|minerais|nutrientes essenciais)", mensagem):
        if "c" in mensagem:
            return "A vitamina C é essencial para o sistema imunológico. Ela pode ser encontrada em frutas cítricas, morangos e pimentões."
        elif "d" in mensagem:
            return "A vitamina D ajuda na absorção de cálcio e saúde óssea. Ela é obtida principalmente pela exposição ao sol e alimentos como ovos e peixes gordurosos."
    elif re.search(r"(suplemento|creatina|bcaa|whey)", mensagem):
        return "Existem diversos tipos de suplementos, como whey protein, creatina, BCAA, e vitaminas. Qual tipo de suplemento você está procurando?"
    
    # Respostas sobre estilo de vida e saúde
    elif re.search(r"(exercício|treino|atividade física|musculação|cardio)", mensagem):
        return "O exercício físico regular é essencial para manter a saúde cardiovascular, força muscular e saúde mental. Recomenda-se pelo menos 30 minutos por dia."
    elif re.search(r"(dieta|alimentação saudável|refeições balanceadas)", mensagem):
        return "Uma dieta equilibrada deve conter todos os macronutrientes essenciais (proteínas, carboidratos e gorduras) e micronutrientes (vitaminas e minerais)."
    elif re.search(r"(hidratação|água|líquidos)", mensagem):
        return "Manter-se hidratado é fundamental para a função corporal adequada. O ideal é consumir pelo menos 2 litros de água por dia."
    
    # Perguntas sobre o funcionamento do chatbot
    elif re.search(r"(chatbot|nutri|ia|inteligência artificial)", mensagem):
        return "Sou o NutriAI, um chatbot especializado em sugerir dietas personalizadas e produtos para você, com base nas suas necessidades e preferências."
    
    # Perguntas sobre como funciona a API
    elif re.search(r"(como funciona|api|integração|shopify)", mensagem):
        return "A API NutriAI se conecta com a Shopify para sugerir produtos e dietas personalizadas com base nas suas necessidades. Você pode me perguntar sobre alimentos, suplementos, e muito mais!"
    
    # Respostas gerais
    elif re.search(r"(ajuda|preciso de ajuda|me ajude)", mensagem):
        return "Claro! Posso te ajudar com informações sobre nutrição, dietas, suplementos e produtos. O que você gostaria de saber?"
    elif re.search(r"(olá|oi|oi chatbot|saudações)", mensagem):
        return "Olá! Como posso te ajudar com sua dieta ou produtos de saúde hoje?"
    
    # Resposta padrão para perguntas não reconhecidas
    return "Desculpe, não entendi sua pergunta. Pode reformular ou pergunte sobre dietas, nutrientes, ou produtos!"

def buscar_produtos(texto: str) -> list:
    """
    Função mock para simular a busca de produtos da Shopify.
    """
    produtos_mock = [
        {"id": 123, "title": "Proteína Whey", "categoria": "suplementos"},
        {"id": 124, "title": "Proteína Vegetal", "categoria": "suplementos"},
        {"id": 125, "title": "Suplemento de Creatina", "categoria": "suplementos"},
        {"id": 126, "title": "Vitamina C", "categoria": "vitaminas"},
        {"id": 127, "title": "Óleo de Peixe", "categoria": "suplementos"},
        {"id": 128, "title": "BCAA", "categoria": "suplementos"},
        {"id": 129, "title": "Chá Verde em Pó", "categoria": "nutrição"},
        {"id": 130, "title": "Pasta Integral", "categoria": "alimentos"},
        {"id": 131, "title": "Arroz Integral", "categoria": "alimentos"},
        {"id": 132, "title": "Batata Doce", "categoria": "alimentos"}
    ]
    
    termos = texto.split()
    produtos_encontrados = []

    # Busca por produtos com base no texto enviado
    for produto in produtos_mock:
        for termo in termos:
            if termo.lower() in produto["title"].lower() or termo.lower() in produto["categoria"].lower():
                produtos_encontrados.append(produto)
                break
    
    # Se nenhum produto for encontrado, podemos sugerir uma categoria geral
    if not produtos_encontrados:
        return [{"id": 999, "title": "Sugestões: Proteínas, Vitaminas, Suplementos e Alimentos Saudáveis"}]
    
    return produtos_encontrados
