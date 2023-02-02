#importing the libraries
import openai
import streamlit as st
from streamlit_chat import message

openai.api_key=st.secrets["api_secret"]

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
     background-image: url("https://wallpaperset.com/w/full/b/d/c/436674.jpg");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>

"""
st.markdown(page_bg_img,unsafe_allow_html=True)

#creating  function which will generate the calls from the api

def main():
    menu=["Home","Mental Health","Health & care"]
    choice=st.sidebar.selectbox("Menu",menu)

    if choice=="Home":
        st.subheader("BroBot🤖")
    elif choice=="mental health":
        st.subheader("Mental Health section")
    elif choice=="Health & Care":
        st.subheader("Health & Care section")

if __name__ =='__main__':
    main()


def generate_response(prompt):
    completions=openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature= 0.5,
    )
    message=completions.choices[0].text
    return message
st.title("Chatbot for Suicide Prevention ")

#storing the chat
if 'generated' not in st.session_state:
    st.session_state['generated'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

def get_text():
    input_text=st.text_input("You: ","Hello, how are you?",key="input")
    return input_text

user_input=get_text()

if user_input:
    output=generate_response(user_input)
    #store the output
    st.session_state.past.append(user_input)
    st.session_state.generated.append(output)

#message(st.session_state["generated"][0],avatar_style="bottts",key=str(0))
#message(st.session_state['past'][0],avatar_style="personas",is_user=True,key=str(0)+'_user')

if st.session_state['generated']:

    for i in range(len(st.session_state['generated'])-1,-1,-1):
         message(st.session_state["generated"][i],avatar_style="bottts", key=str(i))
         message(st.session_state['past'][i], is_user=True,avatar_style="personas", key=str(i) + '_user')