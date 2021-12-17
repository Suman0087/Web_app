<template>
  <div class="nav">
    <a href="#">Home</a>
    <a v-on:click="upload" href="#">Upload</a>
    <a v-on:click="filelists" href="#">PDF Lists</a>

    <a v-on:click="xmllist" href="#">Xml Lists</a>
    <!-- <a v-on:click="xmlupload" href="#">Details Of XML</a> -->
  </div>
</template>

<script>
export default {
  name: "Header",
  methods: {
    upload() {
      this.$router.push({ name: "Upload" });
    },
    filelists() {
      this.$router.push({ name: "FileLists" });
    },
    xmlupload() {
      this.$router.push({ name: "XmlListDetails" });
    },
    xmllist() {
      this.$router.push({ name: "XmlList" });
    },
  },
};
</script>
<style>
.nav {
  background-color: #16a085;
  position: fixed;
  top: 0px;
  width: 100%;
  box-shadow: 0px 4px 4px 0px rgb(0 0 0 / 20%);
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
}
.nav a {
  background-color: #16a085;
  padding-left: 20px;
  color: #f2f2f2;
  margin-right: 5px;
  text-align: left;
  text-decoration: none;
  font-size: 25px;
}
.nav a:hover {
  background-color: darkcyan;
  color: #f2f2f2;
}
</style>