import streamlit as st
import pandas as pd
import numpy as np
import time



"""
## Text manipulation
- normal text
- markdown *_text_*

"""

df = pd.DataFrame({'col1': [1,2,3]})

'''
## Printing df
'''
df

x = 10

'''## Printing variables''' 
st.write('x = ',x) 
'''
----------------
## DataFrame 'style' usecase
'''


dataframe = np.random.randn(10, 20)
st.dataframe(dataframe)



dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))


'''### higlighting maximum column values'''
st.dataframe(dataframe.style.highlight_max(axis=0))


'''-----------'''
'''## Bar Chart'''
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


'''-----------'''
'''## Slider'''
x = st.slider('x') # slider widget
st.write(x, 'squared is', x * x)



'''-----------'''
'''## Dropdown'''

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

'''-----------'''

'''### <--- check Sidebar'''

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

'''-----------'''
'''## Layout'''

left_column, right_column, col_three = st.columns(3)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

with col_three:
    '''works like a charm'''



'''--------'''
'''## Integrating sheets'''
from streamlit_gsheets import GSheetsConnection

# Create a connection object.
conn = st.connection("gsheets", type=GSheetsConnection)

df = conn.read()

# Print results.
for row in df.itertuples():
    st.write(f"{row.name} has a :{row.pet}:")


'''-----------'''
'''## Loading Operations [Progress Bar]'''
    
'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'\

