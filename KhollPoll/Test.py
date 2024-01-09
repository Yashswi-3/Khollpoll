from PIL import Image
import streamlit as st
import plotly.express as px0
import pandas as pd 
import os

st.set_page_config(page_title="Mess Review", page_icon="🍞",layout="wide")

with st.container():
    original_title= "<p style='font-family:CHEDROS; color:purple; font-size: 80px;'>EVENTS</p>"
    st.markdown(original_title, unsafe_allow_html=True)
    #st.markdown("# EVENT ❄")
    search=st.text_input("Search ")
    data=pd.read_csv("user1.csv")
    name=data["Name"]
    date=data["Date"]
    desc=data["Description"]

    for i in range(len(name)):
        if search == name[i]:
            st.write(name[i]+" \n "+date[i]+" \n "+desc[i])



tab1, tab2, tab3 = st.tabs(["<_ _ _Daily Updates_ _ _>", "< _ _Clubs & Chapters_ _ >", "< _ _Review For EVENTS_ _ >"])

with tab1:
    st.header("WIE PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("ss.png",width=500)
            

    with text_column:
            st.subheader("FILS")
            st.write("""
            WIE Is coming with FILS for freelancing, internship, linkedin and startup \n
            Get to Known about the important topics.       
            """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 11 - 12 - 2022  
        AT NLH-103
        """)
    st.header("GFG PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s1.png",width=500)
            

    with text_column:
            st.subheader("SPIN THE CODE")
            st.write("""
            GFG presents SPIN the Code,a team-based contest where team management and speed will shine and be tested\n
            Expierence the industrial simulation with the joyfulness of live audience of your hostel\n
            "Programming is fun because when in doubt,just spin it out".
             """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 01 - 12 - 2022  
        AT ALH-002
        """)

    st.header("ATC PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s5.png",width=500)
            

    with text_column:
            st.subheader("BULLETPROOF")
            st.write("""
             Alan Turing Club get rid of all your fears and insecurities and inspired to work on yourself & make you"BULLETPROOF"\n
            Get ready to know more!.
           """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 28 - 11 - 2022  
        AT ALH-002
        """)


    st.header("CODE_CHEF PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s2.png",width=500)
            

    with text_column:
            st.subheader("SYMPOSIUM")
            st.write("""
              Introducing by Codechef to help you make it big in the world of algorithms,programming and coding contests\n
            " Take a step ahead in coding ".
          """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 13 - 12 - 2022  
        AT NLH-102
        """)
    

    st.header("GDSC AND FULL STACK PRESENT")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s3.png",width=500)
            

    with text_column:
            st.subheader("ANDROID CAMPUS FEST")
            st.write("""
             GDSC in collaboration with FullStack Club is organizing Android Campus Fest to share Modern Android Development(MAD)knowledge\n
            Let's Grab Some Knowledge.
            """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 25 - 11 - 2022  
        AT NLH-101
        """)

    st.header("ANSH PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s6.png",width=500)
            

    with text_column:
            st.subheader("NUKKAD NATAK")
            st.write("""
            Ansh Present a Nukkad NatAK in support of a cause that is important all of us \n
            " DESTIGMATIZING PERIODS ".
            """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 12 - 11 - 2022  
        IN FRONT OF C3
        """)
    
    st.header("CREBRUM PRESENTS")
    image_column, text_column, text1_column = st.columns((2,3,1))
    with image_column:
            st.image("s4.png",width=500)
            

    with text_column:
            st.subheader("THE BOOS & HOOS")
            st.write("""
            Cerebrum presents to you "THE BOOS AND HOOS",an open mic scary storytelling competition\n
             Get ready to participate and shine.
            """)
            st.markdown("[Site LINK...](https://sites.google.com/d/1q7JYm--x3cUfGqZ_ZiaKuNJEBL0Jr117/p/1vpb9wyDlOQnXqZpa88dWMv1TiGHsBUNj/edit)")

    with  text1_column:
        st.write("""
        Date & Venue \n
        ON 31 - 10 - 2022  
        ON OPEN GROUND
        """)


with tab2:
   st.header("BENNETT UNIVERSITY")

   expander = st.expander("Clubs & Chapters")
   expander.write("""
    Ansh\n
    Yoga Club\n
    Silhouette\n
    Astronomy Club\n
    Anime Club\n
    Pulse\n
    Cerebrum Club\n
    Comedy\n
    Art of Living\n
    Sunset Movie\n
    Nomads\n
    Rivaaz\n
    ISAC\n
    Castify\n
    Food & Cuisine\n
    Advaita\n
    SPARK\n
    VERVE\n
""")

   st.header("School of ENGINERRING")

   expander = st.expander("Clubs & Chapters")
   expander.write("""\n
    Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
    BlockChain\n
""")

   st.header("School of LAW")

   expander = st.expander("Clubs & Chapters")
   expander.write("""Moot COURT

""") 

    
   

with tab3:
        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l2.png",width=500)
            

        with text_column:
            st.subheader("IEEE WIE")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")    

        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l6.png",width=500)
            

        with text_column:
            st.subheader("ATC")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l5.png",width=500)
            

        with text_column:
            st.subheader("ANSH")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l1.png",width=500)
            

        with text_column:
            st.subheader("IEEE")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l3.png",width=500)
            

        with text_column:
            st.subheader("CODE CHEF")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)\n
    Geeks for Geeks(GfG)\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")


        image_column, text_column, text1_column = st.columns((2,3,1))
        with image_column:
            st.image("l4.png",width=500)
            

        with text_column:
            st.subheader("Google Developer Student Club(GDSC)")
            expander = st.expander("Clubs & Chapters")
            expander.markdown("""Alan Turing Club(ATC)\n
    CodeChef(CC)_____________________3SRARS\n
    Geeks for Geeks(GfG)_____________2STARSs\n
    Google Developer Student Club(GDSC)\n
    (IEEE)\n
    Women In Engineering(IEE-WIE)\n
    Computer Society of India(CSI)\n
    A Community of Tech Enthusiasts(ACM)\n
    FULL STACK\n
    BU Gamers\n
    Silhouette\n
""")




    

