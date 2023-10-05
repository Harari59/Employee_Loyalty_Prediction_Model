import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

st.header('Welcome to EDA Section')

df = pd.read_csv('aug_train.csv')

df_cardinal = df.drop(['enrollee_id','city'],axis=1)


def klasifikasi_experience(experience):
    if pd.isna(experience):
        pass
    elif experience in ['<1','1', '2', '3','4', '5']:
        return 'Junior'
    elif experience in ['6', '7', '8', '9', '10']:
        return 'Intermediate'
    elif experience in ['11','12','13' ,'14','15']:
        return 'Senior'
    else:
        return 'Veteran'

df_cardinal['experience_category'] = df_cardinal['experience'].apply(klasifikasi_experience)
df_ready = df_cardinal.drop(['experience'],axis=1)




kolom_numerik = ['city_development_index','training_hours','target']
kolom_kategori = [ 'gender', 'relevent_experience',
       'enrolled_university', 'education_level', 'major_discipline',
       'company_size', 'company_type', 'last_new_job',  'experience_category']

#HEATMAP

st.header('HEATMAP CORRELATION')

fig_1 = plt.figure(figsize = (10,10))
sns.heatmap(df_ready[kolom_numerik].corr(),annot=True)
plt.title('HEATMAP')

st.pyplot(fig_1)
with st.expander('Explanation'):
        st.markdown('Heatmap merupakan grafik yang dapat memudahkan seseorang untuk melihat korelasi antar kolom dalam suatu tabel.')
        st.markdown('Di heatmap ini yang menjadi perhatian utama adalah target.')
        st.markdown('Dari beberapa kolom yang memiliki nilai korelasi yang cukup bagus adalah limit balance dengan korelasi senilai 16 persen')

st.header('PRESENTASE KARYAWAN LOYAL DAN TIDAK LOYAL')
fig_2 = plt.figure(figsize=(10,10))

df_ready['target'].value_counts().plot(kind='pie', autopct='%.2f%%')
plt.title('Presentase antara Karyawan Loyal vs Tidak Loyal')


st.pyplot(fig_2)
st.info('Keterangan !!', icon="ℹ️")
st.info('Legend : 1 = Tidak Loyal, 0 = Loyal',icon="ℹ️")
with st.expander('Explanation'):
        st.markdown('Pekerja yang ingin resign atau mencari pekerjaan baru terdapat 25% sedangkan pekerja yang loyal terdapat 75 %. ')


st.header('PERSEBARAN DATA KATEGORIKAL TERHADAP TARGET')

    
def grafik_kategori(feature):
    c1,c2 = st.columns(2)
    with c1: 
        fig_3 = plt.figure(figsize=(10,10))
        sns.countplot(data=df_ready, x=feature, hue='target')
        plt.title('Persebaran Jumlah Data ' )
        plt.xlabel(feature)
        plt.ylabel('Jumlah')
        plt.xticks(rotation=45)
        
        st.pyplot(fig_3)

    with c2:
        fig_4 = plt.figure(figsize=(10,10))
        df_ready[feature].value_counts().plot(kind='pie', autopct='%.2f%%')
        plt.title('Presentase jumlah data')
        st.pyplot(fig_4)

st.markdown('GENDER')
grafik_kategori('gender')
with st.expander('Explanation'):
        st.markdown('Bedasarkan gender telihat bahwa jumlah pria yang ingin resign lebih banyak daripada jumlah pekerja wanita. Namun ini bisa diakibatkan karena jumlah pria juga lebih banyak daripada wanita pada data set ini .')

st.markdown('RELEVENT EXPERIENCE')
grafik_kategori('relevent_experience')
with st.expander('Explanation'):
        st.markdown('Berdasarkan relevent experience terlihat bahwa jumlah pekerja yang memiliki pengalam relevan lebih banyak resign daripada pekerja yang tidak mempunyai pengalaman relevan. Namun hal ini juga bisa terjadi karena jumlah pekerja dengan pengealaman relevan lebih banyak daripada jumlah pekerja yang tidak mempunyai pengalaman relevan.')

st.markdown('ENROLLED UNIVERSITY')
grafik_kategori('enrolled_university')
with st.expander('Explanation'):
        st.markdown('Berdasarkan enrollment university terlihat bahwa jumlah pekerja degan no enrolment merupakan jenis pekerja terbanyak yang ingin melakukan resign. Namun ini juga bisa diakibatkan karena jumlah pekerja yang termasuk dalam jenis pekerja no enrollment adalah jenis pekerja dengan jumlah terbanyak. ')

st.markdown('EDUCATION LEVEL')
grafik_kategori('education_level')
with st.expander('Explanation'):
        st.markdown('Berdasarkan education level terlihat bahwa jumlah pekerja dengan yang memiliki pendidikan graduate adalah jenis pekerja yang paling banyak ingin melakukan resign. Hal ini bisa menandakan bahwa para pekerja dengan  lulusan sarjana terkadang ingin mencoba untuk mencari kesempatan yang lebih luas daripada pekerja dengan level pendidikan yang lain . ')

st.markdown('MAJOR DISCIPLINE')
grafik_kategori('major_discipline')
with st.expander('Explanation'):
        st.markdown('Berdasarkan major discipline terlihat bahwa jumlah pekerja dengan major discipline STEM adalah jenis pekerja yang paling banyak ingin melakukan resign. Namun hal ini juga bisa diakibatkan karena pada data set ini yang memiliki jumlah terbanyak adalah pekerja dengan jurusan STEM. ')

st.markdown('COMPANY SIZE')
grafik_kategori('company_size')
with st.expander('Explanation'):
        st.markdown('Berdasarkan company size pekerja yang paling banyak ingin melakukan resign adalah pekerja yang bekerja pada perusahaan dengan karyawan sebanyak 50-99. Hal ini bisa jadi menandakan bahwa perusahaan dengan jumlah karyawan yang sedikit seperti ini lebih berpeluang untuk kehilangan para pekerjanya. Namun hal ini juga bisa terjadi karena jumlah company size pada dataset ini yang terbanyak adalah perusahaan dengan jumlah karyawan 50-99. ')

st.markdown('COMPANY TYPE')
grafik_kategori('company_type')
with st.expander('Explanation'):
        st.markdown('Bedasarkan type company yang memiliki karyawan paling banyak ingin resign adalah jenis perusahaan PVT. Namun hal ini bisa diakibatkan karena jumlah data pada company type yang terbanyak adalah perusaan berjenis PVT. ')

st.markdown('LAST NEW JOB')
grafik_kategori('last_new_job')
with st.expander('Explanation'):
        st.markdown('Berdasarkan lama bekerja sebelum di perusahaan, karyawan yang paling banyak ingin resign adalah yang karyawan dengan jangka waktu bekerja ditempat sebelumnya di 1 tahun. Hal ini mungkin terjadi karena karyawan baru terkadang belum bisa loyal dengan perusahaan yang baru dan juga memerlukan adaptasi di perusahaan tersebut. ')

st.markdown('EXPERIENCE CATEGORY')
grafik_kategori('experience_category')
with st.expander('Explanation'):
        st.markdown('Berdasarkan experience, karyawan yang paling banyak ingin resign adalah karyawan dengan level experience junior. Hal ini mungkin terjadi karena karyawan pada level junior bisa masih tergiur dengan gaji yang lebih besar di perusahan lain. ')


st.header('SUMMARY')

st.markdown('- Untuk karyawan dengan level junior bisa lebih diperhatikan supaya karyawan/pekerja pada level ini bisa menjadi lebih betah di perusahaan dan menjadi loyal dengan perusahaan. ')

st.markdown('- Untuk karyawan yang baru saja bergabung (dibawah 1 tahun) sebaiknya lebih diperhatikan karena pekerja baru ini memerlukan kenyamanan dilingkungan bekerjanya. Dengan adanya treatment yang baik kepada pekerja baru diharapkan dapat membuat pekerja baru ini menjadi betah dan menjadi pekerja yang loyal. ')

st.markdown('- Untuk karyawan dengan level pendidikan sarjana perlu diperhatikan juga, karena terkadang karyawan dengan level pendidikan sarjana sering ingin mencoba mencari pekerjaan lain. Dengan adanya treatment yang baik kepada karyawan pada level ini diharapkan pekerja sarjana dapat lebih betah dan menjadi loyal. ')

st.markdown('- Untuk jenis perusahaan di tipe kecil, sebaiknya lebih berhati-hati karena banyak pekerja yang ingin resign dari tipe perusahaan berjumlah karyawan kecil ini. ')

    