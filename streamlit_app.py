import streamlit as st
from PIL import Image

with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
# Header 
st.write('''
# Thomas Richardson, Ph.D.
##### *CV* 
''')

image = Image.open('dp.jpeg')
st.image(image, width=300)

st.markdown('## Summary', unsafe_allow_html=True)
st.info('''
- Probably change this ''')

#####################
# Navigation

st.markdown('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">', unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #16A2CB;">
  <a class="navbar-brand" href="https://www.linkedin.com/in/thomas-richardson-datascience/" target="_blank">Thomas Richardson</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="/">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education">Education</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#Projects">Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)

#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)

def txt2(a, b):
  col1, col2 = st.columns([1,4])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)

def txt3(a, b):
  col1, col2 = st.columns([1,2])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)
  
def txt4(a, b, c):
  col1, col2, col3 = st.columns([1.5,2,2])
  with col1:
    st.markdown(f'`{a}`')
  with col2:
    st.markdown(b)
  with col3:
    st.markdown(c)

#####################
st.markdown('''
## Education
''')

txt('**PhD** (Evolutionary Behavioural Science), *The University of Manchester*',
'2017-2021')
st.markdown('''
- Research thesis: `Adaptations for contest competition in human males`.
''')

txt('**MSc** (Psychological research methods), *University of Glasgow*',
'2016-2017')
st.markdown('''
- Achieved a distinction
- Presented my thesis at my field's flagship conference in Vancouver (Human Behaviour and Evolution Society)
''')

txt('**BSc** (Psychology), *University of Sheffield*',
'2012-2015')
st.markdown('''
- Achieved a first class mark, placing second in my class of ~180 students
- Achieved a near perfect mark for my final year research project.
- Was elected Academic officer of the Psychology society, bridging communication between staff and students
''')

#####################
st.markdown('''
## Work Experience
''')

txt('**Data Scientist**, Peak AI',
'October 2021-Present')
st.markdown('''
- Worked with 4 businesses across Retail and Recruitment
- 
- 
- 
''')

txt('**Data Scientist**, Egress Software Technologies, Sheffield',
'July ')
st.markdown('''
- 
- 
- 
- 
- 
''')



#####################
st.markdown('''
## Projects
''')
txt4('Thing I made', 'A description of the thing I made', 'https://www.linkedin.com/in/thomas-richardson-datascience/')


#####################
st.markdown('''
## Skills
''')
txt3('Programming', '`Python`, `R`')
txt3('Data processing/wrangling', '`SQL`, `pandas`, `numpy`,`Tidyverse`')
txt3('Data visualization', '`matplotlib`, `seaborn`, `ggplot2`')
txt3('Machine Learning', '`scikit-learn`')
txt3('Model deployment', '`streamlit`, `Flask`, `R Shiny`, `AWS` ')

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/thomas-richardson-datascience/')
txt2('GitHub', 'https://github.com/Thomas-Richardson')
txt2('Google Scholar','https://scholar.google.co.uk/citations?user=Z2_jROYAAAAJ&hl=en&oi=sra')
txt2('Medium','')
