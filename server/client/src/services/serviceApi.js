import requestHelper from "@/services/requestHelper";

let urlHead = "/api";
if(process.env.NODE_ENV === "development"){
    urlHead = "http://127.0.0.1:8000/api"
}

export default {
    TryLogin(formData){
        return requestHelper({
            url: urlHead + "/user/login",
            method: "post",
            data: formData
        })
    },

    TryRegist(formData){
        return requestHelper({
            url: urlHead + "/user/regist",
            method: "post",
            data: formData
        })
    },
    GoLogout(){
        return requestHelper({
            url: urlHead + "/user/logout",
            method: "post"
        })
    }
}

