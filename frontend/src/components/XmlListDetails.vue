<template>
  <div>
    <Header />
    <div class="container">
      <div class="card-details">
        <h1>{{ details.xml_name}}</h1>
        <h2>Name</h2>
        <p v-for="item in details.xml_name.read_name" :key="item">{{ item}}</p>

        <h2>Title</h2>

        <li>{{ details.read_title }}</li>

        <h2>Division</h2>

        <li>{{ details.read_div }}</li>

        <!-- <li>{{ details.read_title }}</li>
        <li>{{ details.read_div }}</li>-->
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
  name: "XmlList",
  data() {
    return {
      details: "",
      id: "",
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    async getData() {
      this.id = this.$route.query.id;
      await axios

        .get(`http://127.0.0.1:8000/api/xmlupload/${this.id}/`)
        .then((res) => {
          console.log(res.data);
          this.details = res.data;
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