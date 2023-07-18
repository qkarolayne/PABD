import streamlit as st
import controller.cliente as cliente
import services.database as db

import controller.cliente as cliente
def deletar ():
    st.title('Deletar dados')

    with  st.form(key='delet'):
        input_matricula = st.number_input(label= 'Matricula: ')
        button_submit= st.form_submit_button('Deletar')

        if buttom_submit:
            aluno.deletar(int(input_matricula))
            st.success('Aluno excluido com sucesso')


