import Home from "./components/Home.vue";
import Upload from "./components/Upload.vue";
import FileLists from "./components/FileLists.vue"
import XmlListDetails from "./components/XmlListDetails.vue"
import XmlList from "./components/XmlList.vue"


import { createRouter, createWebHistory } from "vue-router";

const routes = [
    {
        name: 'Home',
        component: Home,
        path: '/'
    },
    {
        name: 'Upload',
        component: Upload,
        path: '/upload'
    },
    {
        name: 'FileLists',
        component: FileLists,
        path: '/FileLists'
    },
    {
        name: 'XmlListDetails',
        component: XmlListDetails,
        path: '/XmlListDetails'
    },
    {
        name: 'XmlList',
        component: XmlList,
        path: '/XmlList'
    },

];

const router = createRouter({
    history: createWebHistory(),
    routes,
});

export default router;