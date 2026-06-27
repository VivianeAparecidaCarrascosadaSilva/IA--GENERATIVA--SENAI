   # procoding 
# vou  usar a biblioteca
import streamlit as st


st.title('CALCULADORA...')


n1  = st.number_input('numero:', )
n2  = st.number_input('numero:', value = 0.0)


soma, sub, div, mult = st.columns(4)
if soma.button('Soma'):
    calcular   =  n1  + n2 
    st.success(calcular)
elif sub.button('subtração'):    
    calcular   =  n1  - n2 
    st.success(calcular)    
elif div.button('Divisão'):    
    calcular   =  n1  / n2 
    st.success(calcular)       
elif mult.button('Multiplicação'):    
    calcular   =  n1  * n2 
    st.success(calcular)
    
    
    # -------------------------------------------------------------

st.title('desafio 1: o cartão de visitas digital')  

st.header('cartão de visita')
st.text('isso é um texto')
st.markdown('isso é um paragrafo de comentário')

st.title('desafio 2: formulário de cadastro de usuário')

nome= st.text_input('digite um nome')
idade=st.number_input('digite sua idade',value= 0)
st.checkbox('aceitar os termos')
#if st.button('enviar') and st.checkbox:
enviar=st.button('enviar dados')



#-------------------------------------------------------

st.title( 'desafio 3: seletor de cursos')



