import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('cadastrar alunos')
    cursos = ['informatica', 'mineração']
    
    with st.form(key='insert'):
        input_mat = st.number_input(label='Insira a matricula:', format='%d', step=1)
        input_name = st.text_input(label='Insira o nome:')
        input_age = st.number_input(label='Insira a idade:' , format='%d', step=1)
        input_idt = st.number_input(label='Insira o id da turma:' , format='%d', step=1)
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_mat, input_name, input_age,input_idt)
            st.success('Aluno incluido com sucesso')