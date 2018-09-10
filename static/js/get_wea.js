/**
 * Created by jzhang1529 on 18-9-5.
 */

$(function () {
    setTimeout(get_cnd_cd_pic,0);
    function get_cnd_cd_pic() {
        $img = $('#cond_code').children();
        var url = $img.attr('src');
        $img.load(url);
    }
});