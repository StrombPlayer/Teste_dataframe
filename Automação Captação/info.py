import pandas as pd

def guardar_info(driver, df):
    cpf_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[3]/tbody/tr[1]/td[2]/span[2]')
    cpf_certo = cpf_site.text

    nome_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[3]/tbody/tr[1]/td[1]/span[2]')
    nome_certo = nome_site.text

    endereco_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[3]/tbody/tr[2]/td[1]/span[2]')
    endereco_certo = endereco_site.text

    bairro_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[3]/tbody/tr[2]/td[2]/span[2]')
    bairro_certo = bairro_site.text

    cep_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[3]/tbody/tr[2]/td[3]/span[2]')
    cep_certo = cep_site.text

    cod_prefeitura_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[3]/tbody/tr[1]/td[3]/span[2]')
    cod_prefeitura_certo = cod_prefeitura_site.text

    # Parte do imóvel
    inscricao_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[5]/tbody/tr[1]/td[1]/span[2]')
    inscricao_certo = inscricao_site.text

    quadra_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[5]/tbody/tr[1]/td[2]/span[2]')
    quadra_certo = quadra_site.text

    lote_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[5]/tbody/tr[1]/td[3]/span[2]')
    lote_certo = lote_site.text

    reduzido_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[5]/tbody/tr[1]/td[4]/span[2]')
    reduzido_certo = reduzido_site.text

    endereco_imovel_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[5]/tbody/tr[2]/td[1]/span[2]')
    endereco_imovel_certo = endereco_imovel_site.text

    bairro_imovel_site = driver.find_element_by_xpath('/html/body/div[3]/form/div/table[5]/tbody/tr[2]/td[2]/span[2]')
    bairro_imovel_certo = bairro_imovel_site.text

    all_info = {
        'Cod_Reduzido': reduzido_certo,
        'Insc_Cadastral': inscricao_certo,
        'Imovel_Endereco': endereco_imovel_certo,
        'Bairro': bairro_certo,
        'Quadra': quadra_certo,
        'Lote': lote_certo,
        'Area Territorial': 0, 
        'Area Predial': 0, 
        'Testada': 0,
        'Cod_Prefeitura': cod_prefeitura_certo,
        'Contribuinte_CPF': cpf_certo,
        'Contribuinte_Nome': nome_certo,
        'Contribuinte_Endereco': endereco_certo,
        'Contribuinte_CEP': cep_certo,
        'Bairro_Imovel': bairro_imovel_certo,
        }

    atual = pd.DataFrame.from_dict(all_info, orient='index')
    print(type(atual))   


    #data_list.append(atual)

    #test1 = df.transpose()
    #test2 = atual.transpose(copy=True)
    #test1.to_excel('test1.xlsx')
    #test2.to_excel('test2.xlsx') 