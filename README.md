# Personalized Learning Plan Using Generative AI

**Authors:** Joshua Sirusstara & Kevin Bryan
**Date:** September 2024

## Introduction

Mencari pekerjaan di industri teknologi saat ini semakin menantang, terutama di tengah kondisi "tech winter" dan meningkatnya tuntutan perusahaan terhadap sumber daya manusia. Perkembangan teknologi yang pesat menambah kompleksitas bagi para developer, terutama bagi fresh graduates, yang kesulitan beradaptasi dan bersaing untuk menjadi kandidat yang memenuhi syarat dalam proses rekrutmen.

Di Indonesia, persaingan untuk posisi di industri teknologi semakin ketat, terutama dengan tingginya tingkat pengangguran yang mencapai 7,86 juta orang pada Agustus 2023, lebih tinggi dibandingkan sebelum pandemi COVID-19. Bob Azam dari Apindo mencatat bahwa meskipun jumlah tenaga kerja baru meningkat, penyerapan tenaga kerja, terutama di sektor manufaktur, tidak optimal. Saat ini, pertumbuhan ekonomi hanya menyerap 1 juta pekerja untuk setiap kenaikan 5 persen, dibandingkan dengan 600 ribu pekerja pada era kejayaan manufaktur. Peneliti Indef, Riza Annisa Pujarama, menambahkan bahwa sektor-sektor yang tumbuh pesat, seperti akomodasi, makanan-minuman, serta transportasi dan pergudangan, tidak menyerap tenaga kerja secara proporsional. Banyak lulusan baru yang belum memiliki pengalaman praktis atau akses ke sumber daya yang tepat untuk mengasah keterampilan. Ini membuat mereka kesulitan bersaing dengan kandidat yang lebih berpengalaman atau memiliki latar belakang pendidikan yang lebih kuat. PathEdu hadir untuk menjembatani kesenjangan ini dengan menyediakan panduan dan pelatihan yang sesuai dengan kebutuhan pasar kerja di Indonesia, sehingga pencari kerja dapat meningkatkan kompetensi mereka dan lebih siap menghadapi tantangan di industri teknologi.

## Tujuan dan Manfaat

PathEdu hadir dengan tujuan untuk membimbing para pencari kerja, khususnya di bidang teknologi, dalam mempersiapkan diri untuk posisi yang mereka lamar. Dengan fokus pada penguatan hard skills, PathEdu bertujuan untuk meminimalisir kesulitan dalam beradaptasi dengan peran yang diambil dan membantu calon pekerja siap menghadapi proses wawancara.

## Metodologi dan Cara Kerja

Secara garis besar, PathEdu akan menganalisis pekerjaan yang ingin dilamar oleh pengguna, dengan tujuan untuk memfilter dan mengidentifikasi persyaratan yang dibutuhkan, khususnya yang berkaitan dengan hard skill. Setelah tahap ini, PathEdu akan mencari sumber belajar gratis yang sesuai untuk mendukung persiapan pengguna. Berdasarkan informasi yang diberikan oleh pengguna, PathEdu akan memberikan _learning path_ yang unik sesuai minat dan keahlian user.

![image](https://github.com/user-attachments/assets/31f94fc9-708a-41f8-8317-9450662e64b6)

PathEdu menggunakan arsitektur RAG dan memanfaatkan chaining-retrieval question-answering untuk memastikan learning path yang terstruktur dan terarah. Dokumen berisi material pembelajaran dikumpulkan melalui beberapa sumber seperti YouTube, Udemy, Oreilly untuk mendapatkan gambaran konten pembelajaran berupa text. Kemudian kumpulan text diencode menjadi embedding yang disimpan ke vector storage deep lake.

Saat proses question-answer hasil embedding resource ini akan digunakan sebagai referensi untuk dicantumkan pada step pembelajaran selanjutnya. Step pembelajaran selanjutnya ini dihasilkan secara zero shot berdasarkan pemahaman umum foundation model, prompt tuning dari system, dan augmentasi dari sumber dokumen pembelajaran. Step yang dihasilkan berupa beberapa pilihan topic yang dibangun dari respon user mengenai hal yang sudah dipelajari dari tahapan pembalajaran sebelumnya, sehingga mendukung kebebasan user memilih topik pembelajaran sesuai minat, dengan tetap menjaga bahan pembelajaran yang sesuai dengan konteks pemahaman user.

## Kesimpulan

PathEdu memberikan bantuan kepada para pencari kerja di bidang teknologi dengan menyediakan sumber belajar gratis yang disesuaikan berdasarkan pekerjaan yang dilamar serta tingkat keterampilan pengguna, mulai dari pemula hingga tingkat mahir. Program ini bertujuan untuk mempersiapkan pengguna dalam memenuhi persyaratan hard skill yang dibutuhkan dalam posisi yang mereka inginkan.



