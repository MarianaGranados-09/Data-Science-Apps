#Libraries

from email.mime import image
import imp
from msilib import sequence
from turtle import color
import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dne-brokenNEW.jpg')

st.image(image, use_column_width=True)

st.write( """

    # DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA.
***

"""
)

#Input text box

st.header('Enter DNA sequence')
sequence_input = "Example: DNA Query\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area('Sequence input', sequence_input, height=300)
sequence = sequence.splitlines()
sequence = sequence[1:] #skip sequence name by taking #string from the first position to > final
sequence = ''.join(sequence) #Concatenates list of DNA sequences to string

st.write("""
***
"""
)

#Prints the input DNA sequence

st.header('DNA SEQUENCE: ')
sequence

#DNA nucleotide count
st.write('## OUTPUT (DNA Nucleotide Count)')

#Print Dictionary

st.subheader('1.  Print dictionary')
def DNA_nucleotide_Count(seq):
    DNAdic = dict(
        [
          ('A',seq.count('A')),
          ('T',seq.count('T')),
          ('G',seq.count('G')),
          ('C',seq.count('C'))

        ])
    return DNAdic

#Count number of DNA nucleotide count using dictionary DNAdic from DNA_nucleotide_count function
X = DNA_nucleotide_Count(sequence)

#X_label = list(X)
#X_values = list(X.values())

X

#Print text 
st.subheader('DNA Count')
st.write('There are ' + str(X['A']) + ' adenine (A)')
st.write('There are ' + str(X['T']) + ' thymine (T)')
st.write('There are ' + str(X['G']) + ' guanine (G)')
st.write('There are ' + str(X['C']) + ' cytosine (C)')

### 3. Display DataFrame
st.subheader('DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

### 4. Display Bar Chart using Altair
st.subheader('Bar chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count',
    opacity = alt.value(0.8),
    color=alt.value('red')
)
p = p.properties(
    width=alt.Step(50)  # controls width of bar.
    
)
st.write(p)
