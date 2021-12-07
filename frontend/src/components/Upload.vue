<template>
  <Header />
  <div class="container">
    <div class="form-control">
      <h2 class="heads">Upload File</h2>
      <label>
        Name
        <input type="text" v-model="name" />
      </label>
      <br />
      <br />
      <label>
        Upload PDF File
        <input type="file" @change="handleFileUpload($event)" />
      </label>
      <br />

      <br />
    </div>
    <button class="submit-button" v-on:click="submitFile()">Submit</button>
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
      name: "",
      pdf_file: "",
    };
  },

  methods: {
    handleFileUpload(event) {
      this.document = event.target.files[0];
    },

    submitFile() {
      let formData = new FormData();

      formData.append("name", this.name);
      formData.append("document", this.document);

      axios
        .post("http://127.0.0.1:8000/api/upload/", formData)
        .then(function () {
          console.log("SUCCESS");
        });
    },
  },
};
</script>

<style scoped>
.container {
  background-color: #b4b4b462;
  max-width: 300px;
  margin: 40px auto;
  margin-top: 5rem;
  padding: 30px 20px;
  box-shadow: 2px 5px 10px rgba(0, 0, 0, 0.5);
}
.heads {
  text-align: center;
}
.form-control {
  text-align: left;
  margin-bottom: 25px;
}
.form-control input,
.form-control select,
.form-control textarea {
  border: 1px solid #777;
  border-radius: 4px;
  padding: 10px;
  width: 90%;
}
.submit-button {
  background-color: #16a085;
  border-radius: 5px;
  width: 80px;
  font-size: 20px;
  text-align: center;
}
</style>