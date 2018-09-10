/**
 * Created by jzhang1529 on 18-9-8.
 */

$(function () {

    // 自动联想

    $("#city").keyup(function () {
        $.get("get_loc_ajax/",{"location": $("#city").val()},function (data) {
            $("#city").autocomplete({
                  source: data["location"]
            });

    });
        });

    // 刷新按钮
    $("#rush").click(function () {
        window.location.replace("/")
    });

    // 判断是否为付费项目
    setTimeout(is_free(),100);

    function is_free() {
        if ($("#pm25").html().indexOf("无")>=0){
        alert("暂无该地区空气质量数据。");
    }
    }
});