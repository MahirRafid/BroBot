import requests
import streamlit as st
from streamlit_lottie import st_lottie
import streamlit.components.v1 as components
from PIL import Image

st.set_page_config(
    page_title="Suicide Prevention Chatbot",
    page_icon="🤖"
)

page_bg_img="""
<style>
[data-testid="stAppViewContainer"]{
    background-image: url("https://images.pexels.com/photos/3978594/pexels-photo-3978594.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
    background-size: cover;
}
[data-testid="stHeader"]{
    background-color: rgba(0,0,0,0);
}
</style>

"""
st.markdown(page_bg_img,unsafe_allow_html=True)

st.title("Hello there, I am your BroBot 🤖")
st.sidebar.success("Select a page above.")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ---- https://assets1.lottiefiles.com/packages/lf20_c8s19yot.json
lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_KXdLRdwnM5.json")
img_movie1 = Image.open("images/image1.jpg")
img_movie2 = Image.open("images/image2.webp")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("The best listener in business")
    st.title("By your side for whatever's ahead")
    st.write(
        "Meet BroBot, your personal mental health ally that helps you get back to feeling like yourself."
    )
    st.write("[Learn More >](https://pythonandvba.com)") # remove this line maybe?

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Why should you talk to me?")
        st.write("##")
        st.write(
            """
            - Are you having suicidal thoughts? Talk to me, sharing your pain can be a great way to release the stress.
            - Backed by AI and Psychology, I can help you change your negative thoughts into joyful ones.
            - Want to learn why we feel depressed and suicidal? You are not the only person suffering from problems, but maybe you are one of them who are suffering with how to cope with your problems.
            - You can share absolutely anything, without any fear of privacy breach.
            If this sounds interesting to you, consider giving me a shot, maybe you will end up with a great friend for the rest of your life.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)") # remove this line maybe?
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("Movies you can try")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_movie1)
    with text_column:
        st.subheader("Around the World in 80 Days")
        st.write(
            """
            A Victorian Englishman bets that with the new steamships and railways he can circumnavigate the globe in eighty days.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)") # remove this line maybe? or add netflix link?
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_movie2)
    with text_column:
        st.subheader("The Lion King")
        st.write(
            """
            Lion prince Simba and his father are targeted by his bitter uncle, who wants to ascend the throne himself.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)") # remove this line maybe? or add netflix link?

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/hrithik11804064@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

#---Extensions---

with st.container():
    st.write("---")
    st.header("For some interesting topics...")
    st.write("##")

components.html(
    """
   <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    <div id="accordion mt-5" style="background: black; color: white">
      <div class="card" style="background: #1f1f14; color: white">
        <div class="card-header" id="headingOne">
          <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
            Mental Health - Socio & Legal Services
            </button>
          </h5>
        </div>
        <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
          <div class="card-body">
            The Socio-Legal Center coordinates and facilitates services for persons with mental illness in the criminal justice system, bringing together agencies with a shared interest in ensuring that this population receives appropriate services. Monroe’s Assisted Outpatient Treatment, Transition Management and Medication Grant Programs are also operated at the Socio-Legal Center.
          </div>
        </div>
      </div>
      <div class="card" style="background: #1f1f14; color: white">
        <div class="card-header" id="headingTwo">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
            Association for Suicide Prevention
            </button>
          </h5>
        </div>
        <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
          <div class="card-body">
            You're not alone. Whether you have struggled with suicide yourself or have lost a loved one, know you are not alone. Hear about personal experiences from people in your local community whose lives have been impacted by suicide.
          </div>
        </div>
      </div>
      <div class="card" style="background: #1f1f14; color: white">
        <div class="card-header" id="headingThree">
          <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseThree" aria-expanded="false" aria-controls="collapseTwo">
            Benefits of Mental Wellness
            </button>
          </h5>
        </div>
        <div id="collapseThree" class="collapse" aria-labelledby="headingThree" data-parent="#accordion">
          <div class="card-body">
            Mental wellness gives you a sense of self-worth, dignity, belonging, problem-solving, self-determination, tolerance, acceptance and respect for others so that you can realize your full potential, understand and feel good about yourself, relate to others and expand your social support networks, experience pleasure and enjoyment
            and  handle stress.
          </div>
        </div>
      </div>
    </div>
    """,
    height=600,
)