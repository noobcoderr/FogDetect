/**
 * Created by jzhang1529 on 18-9-5.
 */

$(function () {

    get_tmp_hum();
    setInterval(get_tmp_hum, 10800000);

    function get_tmp_hum() {
    　　function GetUrlParam(paraName) {
    　　　　var url = document.location.toString();
    　　　　var arrObj = url.split("?");

    　　　　if (arrObj.length > 1) {
    　　　　　　var arrPara = arrObj[1].split("&");
    　　　　　　var arr;

    　　　　　　for (var i = 0; i < arrPara.length; i++) {
    　　　　　　　　arr = arrPara[i].split("=");

    　　　　　　　　if (arr != null && arr[0] == paraName) {
    　　　　　　　　　　return arr[1];
    　　　　　　　　}
    　　　　　　}
    　　　　　　return "";
    　　　　}
    　　　　else {
    　　　　　　return "";
    　　　　}
    　　};

        var city = GetUrlParam("city");

        $.getJSON('/get_tmp_hum/',{"location":city}, function (data) {
            var chart = Highcharts.chart('container', {

                chart: {
                    backgroundColor: {
                        linearGradient: [0, 0, 500, 500],
                        stops: [
                            [0, 'rgb(200, 235, 255)'],
				            [1, 'rgb(180, 200, 255)']
                        ]
                    },
                    type: 'line',
                    borderRadius:5
                },
                title: {
                    text: '未来24h温度/湿度'
                },
                credits:{
                     text:"来自和风天气",
                     href:"http://www.heweather.com"
                },
                exporting: { enabled: false },
                xAxis: {
                    categories: data["time_24"]
                },
                yAxis: {
                    title: {
                        text: null
                    }
                },
                plotOptions: {
                    line: {
                        dataLabels: {
                            // 开启数据标签
                            enabled: true
                        },
                        // 关闭鼠标跟踪，对应的提示框、点击事件会失效
                        enableMouseTracking: true
                    }
                },
                series: [{
                    name: '温度(℃)',
                    // data:[7.0, 6.9, 9.5, 14.5, 18.4, 21.5, 25.2, 60]
                    data: data["tmp_24"]
                }, {
                    name: '湿度(%)',
                    // data: [-20, 4.2, 5.7, 8.5, 11.9, 15.2, 17.0, 16.6]
                    data: data["hum_24"]
                }]
            });
        })
    }
});