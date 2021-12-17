<template>
  <div>
    <Header />
    <div class="container">
      <div class="card-details" v-for="item in datas" :key="item">
        <h1>{{ item.xml_name}}</h1>
        <li>{{ item.read_name }}</li>
        <li>{{ item.read_title }}</li>
        <li>{{ item.read_div }}</li>
      </div>
    </div>
  </div>
</template>

<script>
import Header from "./Header.vue";
import axios from "axios";

export default {
  components: {
    Header,
  },
  data() {
    return {
      datas: [],
      showNextButton: false,
      showPreviousButton: false,
      currentPage: 1,
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    goToNextPage() {
      this.currentPage += 1;
      this.getData();
    },
    goToPreviousPage() {
      this.currentPage -= 1;
      this.getData();
    },
    async getData() {
      await axios
        // .get("http://127.0.0.1:8000/api/upload/")

        .get("http://127.0.0.1:8000/api/xmlupload/")
        .then((res) => {
          console.log(res.data);
          this.datas = res.data;
          //   this.datas = res.data.results;
          // console.log(this.info);

          //   if (res.data.next) {
          //     this.showNextButton = true;
          //   }

          //   if (res.data.previous) {
          //     this.showPreviousButton = true;
          //   }
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style>
.container {
  margin-top: 0rem;
  font-size: 15px;
  background-color: #b4b4b462;
  max-width: 300px;
  margin: 40px auto;
  padding: 30px 20px;
}
.card-details {
  justify-content: center;
  text-align: justify;
}
.card-details h1 {
  text-align: center;
}
</style>