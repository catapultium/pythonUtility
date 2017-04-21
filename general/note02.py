#-*- coding: utf-8 -*-

doc = """<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="ko" lang="ko"><head id="ctl00_Head1"><meta http-equiv="X-UA-Compatible" content="IE=5"><title>
	Fly, better fly_ Jin Air
</title><meta content="no" http-equiv="imagetoolbar"><meta content="text/html" charset="utf-8" http-equiv="Content-Type"><meta content="text/javascript" http-equiv="Content-Script-Type"><meta content="text/css" http-equiv="Content-Style-Type"><link rel="SHORTCUT ICON" href="/images/nabi_02_gif_16x16.ico"><link rel="stylesheet" type="text/css" href="/Common/Css/jinair.css"><link rel="stylesheet" type="text/css" href="/Common/Css/point.css"><link rel="stylesheet" href="https://pg.cnspay.co.kr:443/dlp/css/pc/cnspay.css" type="text/css"><link rel="stylesheet" type="text/css" href="/KakaoPay/css/kakaopayDlp.css"><link rel="stylesheet" type="text/css" href="/Common/Css/mainIE.css">

    <script async="" src="//www.google-analytics.com/analytics.js"></script><script type="text/javascript" src="/Script/jquery-1.6.4.min.js"></script>
    <script type="text/javascript" src="/Script/Gnb.js"></script>
    <script src="/Script/swfobject_modified.js" type="text/javascript"></script>
    <script type="text/javascript" src="https://pg.easypay.co.kr/webpay/EasypayCard_Web.js"></script>
    <script type="text/javascript" src="/script/Common.js"></script>
    <script type="text/javascript" src="/script/Validation.js"></script>
    <script type="text/javascript" src="/script/Prototype.js"></script>

    <script type="text/javascript" src="/script/jin_new/jquery-1.10.2.min.js"></script>
    <script type="text/javascript">$110 = jQuery.noConflict();</script>
    <script type="text/javascript" src="/script/jin_new/jquery.placeholder.js"></script>

    <script type="text/javascript">
        $110(function () {
            var title1 = $110("h2 img").attr('alt');
            var title2 = $110("h3 img").attr('alt');
            if ($110("#content_tbl").find("h3").size() == 0) {
                document.title = "Fly, better fly_ Jin Air";
            } else {
                document.title = title2 + "<" + title1 + ":Fly, better fly_ Jin Air";
            }
        });

        $110(function () {
            //gnb
            $110("#gnb li a").bind('mouseenter focusin', function () {
                $110("#gnb li ul").show();
                if ($110('#gnb').hasClass('lang') == 1) {
                    $110("#gnb").stop().animate({ "height": "163px" }, 200);
                } else {
                    $110("#gnb").stop().animate({ "height": "190px" }, 200);
                }
            });
            $110("#gnb").mouseleave(function () {
                $110("#gnb li ul").hide();
                $110("#gnb").stop().animate({ "height": "41px" }, 200);
            });
            $110("#gnb li ul li:last a").focusout(function () {
                $110("#gnb li ul").hide();
                $110("#gnb").stop().animate({ "height": "41px" }, 200);
            });
            $110("#gnb li a").each(function () {
                $110(this).bind('mouseenter focusin', function () {
                    $110(this).find("img").attr("src", function () {
                        return $110(this).attr("src").replace("_off", "_on");
                    });
                }).bind('mouseleave focusout', function () {
                    $110(this).find("img").attr("src", function () {
                        return $110(this).attr("src").replace("_on", "_off");
                    });
                });
            });
            $110("#gnb>li>ul").bind('mouseenter focusin', function () {
                $110(this).parent().find(">a>img").attr("src", function () {
                    return $110(this).attr("src").replace("_off", "_on");
                });
            });
            $110("#gnb>li>ul").bind('mouseleave focusout', function () {
                $110(this).parent().find(">a>img").attr("src", function () {
                    return $110(this).attr("src").replace("_on", "_off");
                });
            });

            //boxShow
            $110(".boxShow").each(function () {
                $110(this).find(">a").bind('mouseenter focusin', function () {
                    $110(this).parent().find("ul").show();
                });
                $110(this).find("ul li:last a").on("keydown", function (e) {
                    if (e.keyCode === 9 && !e.shiftKey) {
                        e.preventDefault();
                        $110(this).parent().parent().parent("li").next("li").find("a").focus();
                        $110(this).parent().parent("ul").hide();
                    }
                });
                $110(this).mouseleave(function () {
                    $110(this).parent().find("ul").hide();
                });
            });

            $110(".utilCont, #footer").find(".boxShow > a").on("keydown", function (e) {
                if (e.keyCode === 9 && e.shiftKey)
                    $110(this).siblings('ul').hide();
            });

            $110("label img").on("click", function () {
                $110("#" + $110(this).parents("label").attr("for")).focus();
            });

            $110("#gnb").each(function () {
                $110(this).find("li:first > a").on("keydown", function (e) {
                    if (e.keyCode === 9 && e.shiftKey) {
                        $110("#gnb").find("ul").hide();
                        $110("#gnb").stop().animate({ "height": "41px" }, 200);
                    }

                });
            });

            $110('.txt').placeholder({ customClass: 'my-placeholder' });

            if ($110('.listTypeD').size() > 0) {
                $110('.listTypeD thead tr').find('th:last-child').addClass('brn');
                $110('.listTypeD tbody').find('tr td:last-child').addClass('brn');
                $110('.listOver tbody td').bind('mouseenter focusin', function () {
                    $110('.listOver tbody tr').removeClass('on');
                    $110(this).parent('tr').addClass('on');
                });
                $110('.listOver tbody td').bind('mouseleave focusout', function () {
                    $110(this).parent('tr').removeClass('on');
                });
            }

            if ($110('#contant').size() > 0 || $110('#contant').height() > $110('#container').height()) {
                var navH = $110('#nav').height();
                $110('#contant .contBg').css('min-height', navH);
            }
        });

        function GreenDonation() {
            window.open("http://gck.kr/greendonation.htm", "GreenDonation", "width=700, height=900, scrollbars=yes");
        }

        function GetTransportTerms(type) {
            var url = "";
            if (type == "DOM")
                url = "/HOM/Service/국내여객운송약관.pdf";
            else
                url = "/HOM/Service/국제여객운송약관.pdf";
            window.open(url, "TransportTerms");
        }

        function GetTransportTermsMultyLang(lang, type) {
            var url = "";
            switch (lang) {

                case "ENG":
                    if (type == "DOM")
                        url = "/Language/ENG/ServiceGuide/General_Conditions_of_Carriage_Domestic.pdf";
                    else
                        url = "/Language/ENG/ServiceGuide/General_Conditions_of_Carriage_International.pdf";
                    break;
                case "CHT":
                    if (type == "DOM")
                        url = "/Language/CHT/ServiceGuide/General_Conditions_of_Carriage_Domestic.pdf";
                    else
                        url = "/Language/CHT/ServiceGuide/General_Conditions_of_Carriage_International.pdf";
                    break;
                case "CHN":
                    if (type == "DOM")
                        url = "/Language/CHN/ServiceGuide/General_Conditions_of_Carriage_Domestic.pdf";
                    else
                        url = "/Language/CHN/ServiceGuide/General_Conditions_of_Carriage_International.pdf";
                    break;
                case "JPN":
                    if (type == "DOM")
                        url = "/Language/JPN/ServiceGuide/General_Conditions_of_Carriage_Domestic.pdf";
                    else
                        url = "/Language/JPN/ServiceGuide/General_Conditions_of_Carriage_International.pdf";
                    break;
                default:

            }

            window.open(url, "TransportTerms");
        }

        function GreenDonation() {
            fn_OpenModaless("http://gck.kr/greendonation.htm", "GreenDonation", "700", "900", "yes");
        }

        function SkipMenu() {
            //$110("#container a").first().focus();

            $110("#content_tbl").attr("tabindex", 0);
            $110("#content_tbl").focus();
        }
    </script>

    <style type="text/css">
        #book {
            position: absolute;
            left: 12px;
            top: 89px;
            width: 274px;
            height: 108px;
            z-index: 1;
        }

        #Flinfo {
            position: absolute;
            left: 239px;
            top: 89px;
            width: 298px;
            height: 28px;
            z-index: 2;
        }

        #Trinfo {
            position: absolute;
            left: 463px;
            top: 89px;
            width: 273px;
            height: 30px;
            z-index: 3;
        }

        #Trservice {
            position: absolute;
            left: 686px;
            top: 89px;
            width: 302px;
            height: 28px;
            z-index: 4;
        }

        #Book_sub {
            position: absolute;
            left: 0;
            top: 34px;
            width: 230px;
            height: 125px;
            z-index: 5;
            visibility: hidden;
        }

        #Flinfo_sub {
            position: absolute;
            left: 228px;
            top: 34px;
            width: 224px;
            height: 73px;
            z-index: 6;
            visibility: hidden;
        }

        #Trinfo_sub {
            position: absolute;
            left: 452px;
            top: 34px;
            width: 224px;
            height: 96px;
            z-index: 7;
            visibility: hidden;
        }

        #Trservice_sub {
            position: absolute;
            left: 676px;
            top: 40px;
            width: 224px;
            height: 116px;
            z-index: 8;
            visibility: hidden;
        }

        .hide_el,
        .jiniPlus_title {
            overflow: hidden;
            position: absolute;
            width: 1px;
            height: 1px;
            border: none;
            clip: rect(1px 1px 1px 1px);
            clip: rect(1px, 1px, 1px, 1px);
        }

        .refund_tbl thead th {
            padding: 7px 0;
        }

        .refund_tbl tbody td {
            text-align: center;
            letter-spacing: -1px;
            padding: 7px 0;
            border-bottom: 1px solid #cbe39d;
        }

            .refund_tbl tbody td:first-child {
                border-right: 1px solid #cbe39d;
            }

        .t_header, th {
            font-weight: normal;
        }

        .rsv_title {
            text-align: left;
        }
    </style>

    <script type="text/javascript">
        var selectIndex = '';
        var selectSubIndex = '';

        function GreenDonation() {
            fn_OpenModaless("http://gck.kr/greendonation.htm", "GreenDonation", "700", "900", "yes");
        }

        function Greenwings() {
            window.open("http://greenwings.jinair.com", "Greenwings");
        }

















    </script>

</head>
<body>
    <div style="display: none;">
        
    <div style="display: none">
        
        <form name="frm_pay" id="frm_pay" method="post">
            <!-- [START]가맹점 주문자 필드(승인요청 시 해당 정보를 부가정보로 사용) -->
            <!--[선택]가맹점 고객일련번호 -->
            <input type="hidden" id="memb_user_no" name="memb_user_no" value="">
            <!--[선택]고객ID -->
            <input type="hidden" id="user_id" name="user_id" value="">
            <!--[선택]고객명 -->
            <input type="hidden" id="user_nm" name="user_nm" value="">
            <!--[선택]고객 E-mail -->
            <input type="hidden" id="user_mail" name="user_mail" value="">
            <!--[선택]가맹점 고객 연락처1 -->
            <input type="hidden" id="user_phone1" name="user_phone1" value="">
            <!--[선택]가맹점필드1 -->
            <input type="hidden" id="user_define1" name="user_define1" value="">
            <!--[선택]가맹점필드2 -->
            <input type="hidden" id="user_define2" name="user_define2" value="">
            <!--[선택]가맹점필드3 -->
            <input type="hidden" id="user_define3" name="user_define3" value="">
            <!--[선택]가맹점필드4 -->
            <input type="hidden" id="user_define4" name="user_define4" value="">
            <!--[선택]가맹점필드5 -->
            <input type="hidden" id="user_define5" name="user_define5" value="">
            <!--[선택]가맹점필드6 -->
            <input type="hidden" id="user_define6" name="user_define6" value="">
            <!-- [END]가맹점 주문자 필드 -->

            <!-- [START]인증 요청 필드 -->
            <!--[필수]가맹점명 -->
            <input type="hidden" id="EP_mall_nm" name="EP_mall_nm" value="Jin Air">
            <!--[필수]가맹점 주문번호(인증응답) -->
            <input type="hidden" id="EP_order_no" name="EP_order_no" value="">
            <!--[선택]상품명 -->
            <input type="hidden" id="EP_product_nm" name="EP_product_nm" value="">
            <!--[필수]상품금액 -->
            <input type="hidden" id="EP_product_amt" name="EP_product_amt" value="">
            <!--[선택]가맹점 페이지 charset(EUC-KR/UTF-8) -->
            <input type="hidden" id="EP_charset" name="EP_charset" value="EUC-KR">
            <!--[필수]가맹점 리턴URL -->
            <input type="hidden" id="EP_return_url" name="EP_return_url" value="https://www.jinair.com/Easypay/card_res.aspx">
            <!--[필수]카드사 코드(인증응답) -->
            <input type="hidden" id="EP_card_cd" name="EP_card_cd" value="">
            <!--[필수]할부개월(인증응답) -->
            <input type="hidden" id="EP_install_period" name="EP_install_period" value="">
            <!--[필수]통화코드(수정불가) -->
            <input type="hidden" id="EP_currency" name="EP_currency" value="00">
            <!--[선택]ISP PGID -->
            <input type="hidden" id="EP_kvp_pgid" name="EP_kvp_pgid" value="A0042">
            <!--[선택]국민 앱카드 결제화면 노출여부(Y:앱카드결제 노출) -->
            <input type="hidden" id="EP_kmotion_useyn" name="EP_kmotion_useyn" value="Y">
            <!--[선택]세이브결제 유무 -->
            <input type="hidden" id="EP_save_useyn" name="EP_save_useyn" value="">
            <!--[선택]카드사 포인트 사용유무 -->
            <input type="hidden" id="EP_point_useyn" name="EP_point_useyn" value="">
            <!--[선택]무이자 유무 -->
            <input type="hidden" id="EP_noint_yn" name="EP_noint_yn" value="">
            <!--[선택]가맹점 사업자번호 -->
            <input type="hidden" id="EP_buss_no" name="EP_buss_no" value="">
            <!--[선택]카드사 가맹점 번호 -->
            <input type="hidden" id="EP_card_join_no" name="EP_card_join_no" value="">
            <!-- VAN모듈 사용여무-->
            <input type="hidden" id="EV_used_van" name="EV_used_van" value="Y">
            <!-- KVP PGID // -->
            <input type="hidden" id="EV_kvp_pgid" name="EV_kvp_pgid" value="A0042">
            <!-- [END]인증 요청 필드-->

            <!-- [START]인증 응답 필드 -->
            <!-- 공통 -->
            <!-- [필수]응답코드 -->
            <input type="hidden" id="EP_res_cd" name="EP_res_cd" value="">
            <!-- [필수]응답메시지 -->
            <input type="hidden" id="EP_res_msg" name="EP_res_msg" value="">
            <!-- [필수]처리구분 -->
            <input type="hidden" id="EP_tr_cd" name="EP_tr_cd" value="">
            <!-- [필수]PG거래번호 -->
            <input type="hidden" id="EP_cno" name="EP_cno" value="">
            <!-- [필수]이지페이 버전 -->
            <input type="hidden" id="EP_client_version" name="EP_client_version" value="">
            <!-- [필수]카드결제종류  -->
            <input type="hidden" id="EP_req_type" name="EP_req_type" value="">
            <!-- [필수]카드결제금액 -->
            <input type="hidden" id="EP_card_amt" name="EP_card_amt" value="">
            <!-- [필수]무이자여부-->
            <input type="hidden" id="EP_noint" name="EP_noint" value="">

            <!-- 안심클릭 -->
            <!-- [선택]안심클릭카드번호 -->
            <input type="hidden" id="EP_card_no" name="EP_card_no" value="">
            <!-- [선택]안심클릭 인증값 -->
            <input type="hidden" id="EP_cavv" name="EP_cavv" value="">
            <!-- [선택]안심클릭 인증값 -->
            <input type="hidden" id="EP_xid" name="EP_xid" value="">
            <!-- [선택]안심클릭 인증값 -->
            <input type="hidden" id="EP_eci" name="EP_eci" value="">
            <!-- [선택]세이브 사용유무(하나/외환)-->
            <input type="hidden" id="EP_ret_save_used" name="EP_ret_save_used" value="">
            <!-- [선택]세이브 종류 (40:부분세이브/41:전체세이브) -->
            <input type="hidden" id="EP_ret_save_kind" name="EP_ret_save_kind" value="">

            <!-- ISP -->
            <!-- [선택]KVP 카드정보 -->
            <input type="hidden" id="EP_kvp_cardcode" name="EP_kvp_cardcode" value="">
            <!-- [선택]KVP 암호화키 -->
            <input type="hidden" id="EP_kvp_sessionkey" name="EP_kvp_sessionkey" value="">
            <!-- [선택]KVP 암호화전문 -->
            <input type="hidden" id="EP_kvp_encdata" name="EP_kvp_encdata" value="">
            <!-- [선택]KVP 포인트플래그 -->
            <input type="hidden" id="EP_kvp_payset_flag" name="EP_kvp_payset_flag" value="">
            <!-- [선택]KVP 포인트 사용금액 -->
            <input type="hidden" id="EP_kvp_using_point" name="EP_kvp_using_point" value="">
            <!-- [선택]KVP 세이브 결제 유무 -->
            <input type="hidden" id="EP_vp_ret_save_point" name="EP_vp_ret_save_point" value="">
            <!-- [선택]KVP 할부개월 -->
            <input type="hidden" id="EP_kvp_quota" name="EP_kvp_quota" value="">
            <!-- [선택]KVP 무이자여부 -->
            <input type="hidden" id="EP_kvp_noint" name="EP_kvp_noint" value="">
            <!-- [선택]카드 BIN(6자리) -->
            <input type="hidden" id="EP_kvp_card_prefix" name="EP_kvp_card_prefix" value="">
            <input type="hidden" id="EP_mall_id" name="EP_mall_id" value="05515137">
            <input type="hidden" id="EP_window_type" name="EP_window_type" value="popup">
        </form>
        <!-- [END]인증 응답 필드 -->


        <script type="text/javascript" src="https://www.bankpay.or.kr/BankPayEFT_UTF8_SSL.js"></script>
        <script type="text/javascript" src="https://pg.easypay.co.kr/webpay/EasypayCard_Web.js"></script>
        <script type="text/javascript">
            //실시간 계좌이체 플러그인 설치
            if (isIE() && "KOR" == "KOR") {
                InstallCertManager();
                SmartUpdate();
            }
        </script>

        <form name="bankRequestForm" id="bankRequestForm" method="post" action="">
            <input type="hidden" name="tx_bank_test" id="tx_bank_test" value="N">
            <input type="hidden" name="hd_pre_msg_type" id="hd_pre_msg_type" value="EFT">
            <input type="hidden" name="hd_msg_code" id="hd_msg_code" value="0200">
            <input type="hidden" name="hd_msg_type" id="hd_msg_type" value="EFT">
            <input type="hidden" name="hd_ep_type" id="hd_ep_type" value="CERT">
            <input type="hidden" name="hd_pi" id="hd_pi">
            <input type="hidden" name="hd_approve_no" id="hd_approve_no" value="14001251">
            <input type="hidden" name="hd_serial_no" id="hd_serial_no" value="6176543">
            <input type="hidden" name="hd_firm_name" id="hd_firm_name" value="진에어">
            <input type="hidden" name="hd_input_option" id="hd_input_option" value="23">
            <input type="hidden" name="hd_ep_option" id="hd_ep_option" value="213">
            <input type="hidden" name="tx_amount" id="tx_amount" value="">
            <input type="hidden" name="tx_user_define" id="tx_user_define" value="">
            <input type="hidden" name="hd_timeout_yn" id="hd_timeout_yn" value="N">
            <input type="hidden" name="hd_timeout" id="hd_timeout" value="300000">
            <input type="hidden" name="tx_bill_yn" id="tx_bill_yn" value="Y">
            <input type="hidden" name="tx_email_addr" id="tx_email_addr" value="">
        </form>
    </div>

    </div>
    <form name="aspnetForm" method="post" action="Reservation.aspx" id="aspnetForm" enctype="multipart/form-data">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwULLTE0ODgxNTUzNjIPZBYCZg9kFgICBQ9kFgoCAQ8PFgQeCEltYWdlVXJsBRwvaW1hZ2VzL25ld01haW4vdG9wX2pvaW4uZ2lmHg1BbHRlcm5hdGVUZXh0BQztmozsm5DqsIDsnoVkZAICDw8WBB8ABR0vaW1hZ2VzL25ld01haW4vdG9wX2xvZ2luLmdpZh8BBQnroZzqt7jsnbhkZAIDDw8WAh4EVGV4dGVkZAIFD2QWAgIBD2QWDAIDDw8WAh8ABSMvaW1hZ2VzL2xlZnRfbWVudS9Cb29rX21lbnUxX3VwLmdpZhYEHgpvbm1vdXNlb3V0BS50aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvQm9va19tZW51MV91cC5naWYnHgtvbm1vdXNlb3ZlcgUudGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0Jvb2tfbWVudTFfdXAuZ2lmJ2QCBQ9kFgQCAQ8PZBYEHwMFMHRoaXMuc3JjPScvaW1hZ2VzL2xlZnRfbWVudS9Cb29rX21lbnUxX3N1YjEuZ2lmJx8EBTN0aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvQm9va19tZW51MV9zdWIxX3VwLmdpZidkAgMPD2QWBB8DBTB0aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvQm9va19tZW51MV9zdWIyLmdpZicfBAUzdGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0Jvb2tfbWVudTFfc3ViMl91cC5naWYnZAIHDw9kFgQfAwUrdGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0Jvb2tfbWVudTIuZ2lmJx8EBS50aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvQm9va19tZW51Ml91cC5naWYnZAILDw9kFgQfAwUrdGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0Jvb2tfbWVudTQuZ2lmJx8EBS50aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvQm9va19tZW51NF91cC5naWYnZAIND2QWBAIBDw9kFgQfAwUudGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0xlZnRfbWVudV9kb20uZ2lmJx8EBTF0aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvTGVmdF9tZW51X2RvbV91cC5naWYnZAIDDw9kFgQfAwUudGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0xlZnRfbWVudV9pbnQuZ2lmJx8EBTF0aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvTGVmdF9tZW51X2ludF91cC5naWYnZAIPDw9kFgQfAwUrdGhpcy5zcmM9Jy9pbWFnZXMvbGVmdF9tZW51L0Jvb2tfbWVudTUuZ2lmJx8EBS50aGlzLnNyYz0nL2ltYWdlcy9sZWZ0X21lbnUvQm9va19tZW51NV91cC5naWYnZAIGD2QWKAIBDw9kFgIeB29uY2xpY2sFV2lmKCFmbl9WYWxpZF9VcERvd25fRGF0ZSgnY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZScsIC0xKSkgcmV0dXJuIGZhbHNlO2QCAg8WAh4JaW5uZXJodG1sBRUwNOyblCAyOOydvCDquIjsmpTsnbxkAgMPD2QWAh8FBVZpZighZm5fVmFsaWRfVXBEb3duX0RhdGUoJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAxKSkgcmV0dXJuIGZhbHNlO2QCBA9kFghmD2QWAmYPZBYCZg9kFgYCAQ8PFgIfAgUP7KCc7KO84oaS6rmA7Y+sZGQCAg8PFgIfAgUJ6rCA64qU7Y64ZGQCAw8WBB4KRGF0YU1lbWJlcgUCT1ceC18hSXRlbUNvdW50AhEWIgIBD2QWBGYPFQcGTEowMzAyCzA3OjA1LTA4OjEwATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwNzA1JywgJzA3MDUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwNzA1JywgJzA3MDUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjI0LDgwMOybkCI+IDI0LDgwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIDD2QWBGYPFQcGTEowMzA0CzA4OjA1LTA5OjE1ATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwODEwJywgJzA4MTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwODEwJywgJzA4MTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjI0LDgwMOybkCI+IDI0LDgwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIFD2QWBGYPFQcGTEowMzA2CzA4OjI1LTA5OjM1ATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwODI1JywgJzA4MjUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwODI1JywgJzA4MjUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjI0LDgwMOybkCI+IDI0LDgwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIHD2QWBGYPFQcGTEowMzA4CzA5OjEwLTEwOjIwATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwOTEwJywgJzA5MTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcwOTEwJywgJzA5MTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjM0LDQwMOybkCI+IDM0LDQwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIJD2QWBGYPFQcGTEowMzE0CzExOjUwLTEyOjU1ATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxMTUwJywgJzExNTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxMTUwJywgJzExNTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjQ2LDQwMOybkCI+IDQ2LDQwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAILD2QWBGYPFQcGTEowMzE2CzEyOjI1LTEzOjM1ATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxMjI1JywgJzEyMjUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxMjI1JywgJzEyMjUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjUxLDIwMOybkCI+IDUxLDIwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIND2QWBGYPFQcGTEowMzE4CzEzOjE1LTE0OjI1ATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxMzE1JywgJzEzMTUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxMzE1JywgJzEzMTUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjYwLDgwMOybkCI+IDYwLDgwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIPD2QWBGYPFQcGTEowMzIwCzE0OjAwLTE1OjA1ATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxNDAwJywgJzE0MDAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzgAZAIRD2QWBGYPFQcGTEowMzI0CzE1OjI1LTE2OjM1ATABMAJGTwM3Mzj3AzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxNTI1JywgJzE1MjUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzAnLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6bm9uZTsiIGRpc2FibGVkIHRpdGxlPSI4MCwwMDDsm5AiPjxmb250IGNsYXNzPSJNYm9vayIgc3R5bGU9ImZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7Ij7rp6Tsp4Q8L2ZvbnQ+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzgAZAITD2QWBGYPFQcGTEowMzI2CzE1OjMwLTE2OjQwATABMAJGTwM3Mzj3AzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxNTMwJywgJzE1MzAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzAnLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6bm9uZTsiIGRpc2FibGVkIHRpdGxlPSI4MCwwMDDsm5AiPjxmb250IGNsYXNzPSJNYm9vayIgc3R5bGU9ImZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7Ij7rp6Tsp4Q8L2ZvbnQ+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzgAZAIVD2QWBGYPFQcGTEowMzI4CzE2OjI1LTE3OjM1ATABMAJGTwM3NzL3AzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxNjI1JywgJzE2MjUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzAnLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6bm9uZTsiIGRpc2FibGVkIHRpdGxlPSI4MCwwMDDsm5AiPjxmb250IGNsYXNzPSJNYm9vayIgc3R5bGU9ImZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7Ij7rp6Tsp4Q8L2ZvbnQ+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3NzIAZAIXD2QWBGYPFQcGTEowMzMwCzE2OjUwLTE4OjAwATABMAJGTwM3Mzj6AzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxNjUwJywgJzE2NTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJy0xMzMnLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6bm9uZTsiIGRpc2FibGVkIHRpdGxlPSI4MCwwMDDsm5AiPjxmb250IGNsYXNzPSJNYm9vayIgc3R5bGU9ImZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7Ij7rp6Tsp4Q8L2ZvbnQ+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzgAZAIZD2QWBGYPFQcGTEowMzMyCzE3OjQwLTE4OjUwATABMAJGTwM3Mzj6AzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxNzQwJywgJzE3NDAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJy0xMzMnLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6bm9uZTsiIGRpc2FibGVkIHRpdGxlPSI4MCwwMDDsm5AiPjxmb250IGNsYXNzPSJNYm9vayIgc3R5bGU9ImZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7Ij7rp6Tsp4Q8L2ZvbnQ+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzgAZAIbD2QWBGYPFQcGTEowMzM2CzE5OjMwLTIwOjQwATABMAJGTwM3Mzj3AzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcxOTMwJywgJzE5MzAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzAnLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6bm9uZTsiIGRpc2FibGVkIHRpdGxlPSI4MCwwMDDsm5AiPjxmb250IGNsYXNzPSJNYm9vayIgc3R5bGU9ImZvbnQtc2l6ZTogMTFweDsgbGV0dGVyLXNwYWNpbmc6IC0xcHg7Ij7rp6Tsp4Q8L2ZvbnQ+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzgAZAIdD2QWBGYPFQcGTEowMzM4CzIwOjQwLTIxOjUwATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcyMDQwJywgJzIwNDAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3NzKgAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcyMDQwJywgJzIwNDAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3NzIsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9Ijc2LDAwMOybkCI+IDc2LDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIfD2QWBGYPFQcGTEowMzQwCzIxOjA1LTIyOjE1ATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcyMTA1JywgJzIxMDUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcyMTA1JywgJzIxMDUnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9Ijc2LDAwMOybkCI+IDc2LDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIhD2QWBGYPFQcGTEowMzM0CzIxOjEwLTIyOjIwATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcyMTEwJywgJzIxMTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJZIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9IjgwLDAwMOybkCI+IDgwLDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAIBDxUFATABMAJGTwM3MzigAzxsYWJlbCBvbmNsaWNrPSJmbl9SYWRpb19DbGljayhldmVudCwgJ2N0bDAwX0NvbnRlbnRQbGFjZUhvbGRlcjFfZmx0bHN0RG93bkxpbmUnLCAnICcsICcyMTEwJywgJzIxMTAnICk7ICIgc3R5bGU9ImN1cnNvcjpwb2ludGVyOyB2ZXJ0aWNhbC1hbGlnbjptaWRkbGU7IiBvbm1vdXNlb3Zlcj0iZm5fU2VhdENudFZpZXcoJzknLCA3MzgsIGV2ZW50KTsiIG9ubW91c2VvdXQ9ImZuX1NlYXRDbnRIaWRlKGV2ZW50KTsiPg0KCQkJCQkJCQkJCQk8aW5wdXQgbmFtZT0icmRvY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZSIgdHlwZT0icmFkaW8iIHZhbHVlPSJFIiBzdHlsZT0iaGVpZ2h0OjEzcHg7IGRpc3BsYXk6aW5saW5lOyIgdGl0bGU9Ijc2LDAwMOybkCI+IDc2LDAwMOybkA0KCQkJCQkJCQkJCTwvbGFiZWw+ZAICDxYCHgVzdHlsZQU0dmVydGljYWwtYWxpZ246bWlkZGxlO21hcmdpbi1ib3R0b206MjU7ZGlzcGxheTpub25lO2QCBA8PZBYCHwkFDGRpc3BsYXk6bm9uZWQCBg8WBB8JBQxkaXNwbGF5Om5vbmUfBQU+Zm5fR2V0RmFyZSgnY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3REb3duTGluZScsIGV2ZW50KTtkAgUPDxYCHgdWaXNpYmxlaBYCHwUFVWlmKCFmbl9WYWxpZF9VcERvd25fRGF0ZSgnY3RsMDBfQ29udGVudFBsYWNlSG9sZGVyMV9mbHRsc3RVcExpbmUnLCAtMSkpIHJldHVybiBmYWxzZTtkAgcPDxYCHwpoFgIfBQVUaWYoIWZuX1ZhbGlkX1VwRG93bl9EYXRlKCdjdGwwMF9Db250ZW50UGxhY2VIb2xkZXIxX2ZsdGxzdFVwTGluZScsIDEpKSByZXR1cm4gZmFsc2U7ZAIID2QWBmYPFgIfCQUNZGlzcGxheTpub25lOxYCZg9kFgJmD2QWBgIBDw8WAh8CBQ/quYDtj6zihpLsoJzso7xkZAICDw8WAh8CBQnsmKTripTtjrhkZAIDDxYGHwcFAlJUHwgCEB8KaBYgAgEPZBYEZg8VBwZMSjAzMDELMDY6MTUtMDc6MjABMAEwAlBEAzc3Mgk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAgMPZBYEZg8VBwZMSjAzMDMLMDY6MjUtMDc6MzABMAEwAlBEAzc3Mgk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAgUPZBYEZg8VBwZMSjAzMDULMDg6MDAtMDk6MTABMAEwAlBEAzczOAk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAgcPZBYEZg8VBwZMSjAzMDcLMDg6NDUtMDk6NTUBMAEwAlBEAzczOAk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAgkPZBYEZg8VBwZMSjAzMDkLMTA6MDAtMTE6MDUBMAEwAlBEAzc3Mgk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAgsPZBYEZg8VBwZMSjAzMTELMTA6MjUtMTE6MzUBMAEwAlBEAzc3Mgk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAg0PZBYEZg8VBwZMSjAzMTMLMTA6NTUtMTI6MDUBMAEwAlBEAzczOAk5Nyw3MDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAg8PZBYEZg8VBwZMSjAzMTkLMTM6NDAtMTQ6NDUBMAEwAlBEAzc3Mgk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAhEPZBYEZg8VBwZMSjAzMjELMTQ6MjUtMTU6MzABMAEwAlBEAzc3Mgk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAhMPZBYEZg8VBwZMSjAzMjMLMTQ6NTUtMTY6MDABMAEwAlBEAzczOAk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAhUPZBYEZg8VBwZMSjAzMjULMTU6MjUtMTY6MzUBMAEwAlBEAzczOAk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAhcPZBYEZg8VBwZMSjAzMjkLMTc6MTUtMTg6MjUBMAEwAlBEAzczOAk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAhkPZBYEZg8VBwZMSjAzMzELMTc6MjUtMTg6MzABMAEwAlBEAzc3Mgk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAhsPZBYEZg8VBwZMSjAzMzMLMTg6MzAtMTk6NDABMAEwAlBEAzc3Mgk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzc3MgBkAh0PZBYEZg8VBwZMSjAzMzULMTk6MjUtMjA6MzUBMAEwAlBEAzczOAk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAh8PZBYEZg8VBwZMSjAzNDELMjA6MDUtMjE6MTABMAEwAlBEAzczOAk4MCwwMDDsm5BkAgEPFQUBMAEwAlBEAzczOABkAgQPD2QWAh8JBQxkaXNwbGF5Om5vbmVkAgYPFgIfCQUMZGlzcGxheTpub25lZAI4D2QWAmYPZBYCAgEPEA8WAh8KaGRkZGQCOQ9kFgJmD2QWAgIDDw9kFgIfBQUoaWYoIWZuX1ZhbGlkYXRpb25fTG9naW4oKSkgcmV0dXJuIGZhbHNlO2QCOg8WAh8JBQ1kaXNwbGF5Om5vbmU7FgJmD2QWBAIBDxAPZBYCHghvbmNoYW5nZQUbZm5fZGRsQ291cG9uX0NoYW5nZShldmVudCk7ZGRkAgMPDxYCHwJlZGQCOw8WAh8JBQ1kaXNwbGF5Om5vbmU7FgJmD2QWBgIDDxAPZBYCHwsFHmZuX2RkbEFEaXNjb3VudF9DaGFuZ2UoZXZlbnQpO2RkZAIFDxAPZBYCHwUFHmZuX2RkbEFEaXNjb3VudF9DaGFuZ2UoZXZlbnQpO2RkZAIHDxAPZBYCHwUFHmZuX2RkbEFEaXNjb3VudF9DaGFuZ2UoZXZlbnQpO2RkZAI9DxYEHwgCAR8KaBYCAgEPZBYOZg8VAQVBZHVsdGQCAw8WAh4FdmFsdWUFB+yEseyduDFkAgQPFQEH7ISx7J24MWQCBQ8QDxYCHgtfIURhdGFCb3VuZGdkZBYBZmQCEQ8QFgIfDWdkFCsBAGQCEw8QFgIfDWdkFCsBAGQCFQ8QFgIfDWdkFCsBAGQCPg8WAh8JBQ1kaXNwbGF5Om5vbmU7FgJmD2QWBgIDD2QWAgIBD2QWAgIBDxAPZBYCHwsFG2ZuX2RkbEdyb3VwX0d1YnVuX0NoYW5nZSgpO2RkZAIHDw9kFgIfCQUKd2lkdGg6OTUlO2QCCw8PZBYCHwkFCndpZHRoOjk1JTtkAj8PFgIfCQUNZGlzcGxheTpub25lOxYCZg9kFhgCAQ8QD2QWAh8FBRxqYXZhc2NyaXB0OlNldEFjY291bnRUeXBlKCk7ZGRkAgMPEA8WAh8KaBYCHwUFHGphdmFzY3JpcHQ6U2V0QWNjb3VudFR5cGUoKTtkZGQCBQ8QD2QWAh8FBRxqYXZhc2NyaXB0OlNldEFjY291bnRUeXBlKCk7ZGRkAgcPEA9kFgIfBQUcamF2YXNjcmlwdDpTZXRBY2NvdW50VHlwZSgpO2RkZAIJDxAPZBYCHwUFHGphdmFzY3JpcHQ6U2V0QWNjb3VudFR5cGUoKTtkZGQCCw8QDxYCHgdDaGVja2VkaBYCHwUFG2phdmFzY3JpcHQ6Q2xpY2tDaGtQb2ludCgpO2RkZAIXDw9kFgYeCm9ua2V5cHJlc3MFHWZuX0NoZWNrTnVtYmVyVGV4dEJveChldmVudCk7HwkFEXRleHQtYWxpZ246cmlnaHQ7HgdvbmtleXVwBS1mbl9OZXh0Rm9jdXMoJ3R4dENhcmRObzAxJywgJ3R4dENhcmRObzAyJywgNClkAhkPD2QWBh8PBR1mbl9DaGVja051bWJlclRleHRCb3goZXZlbnQpOx8JBRF0ZXh0LWFsaWduOnJpZ2h0Ox8QBS1mbl9OZXh0Rm9jdXMoJ3R4dENhcmRObzAyJywgJ3R4dENhcmRObzAzJywgNClkAhsPD2QWBh8PBR1mbl9DaGVja051bWJlclRleHRCb3goZXZlbnQpOx8JBRF0ZXh0LWFsaWduOnJpZ2h0Ox8QBS1mbl9OZXh0Rm9jdXMoJ3R4dENhcmRObzAzJywgJ3R4dENhcmRObzA0JywgNClkAh0PD2QWBh8PBR1mbl9DaGVja051bWJlclRleHRCb3goZXZlbnQpOx8JBRF0ZXh0LWFsaWduOnJpZ2h0Ox8QBTBmbl9OZXh0Rm9jdXMoJ3R4dENhcmRObzA0JywgJ2RkbEV4cERhdGVZZWFyJywgNClkAikPD2QWBh8PBR1mbl9DaGVja051bWJlclRleHRCb3goZXZlbnQpOx8JBRF0ZXh0LWFsaWduOnJpZ2h0Ox8QBS1mbl9OZXh0Rm9jdXMoJ3R4dENhcmRQYXNzd2QnLCAndHh0QXV0aE5vJywgMilkAi0PD2QWBB8PBR1mbl9DaGVja051bWJlclRleHRCb3goZXZlbnQpOx8JBRF0ZXh0LWFsaWduOnJpZ2h0O2QCQA8WAh8KaGQCQQ8PFgIfCmhkZAJCDw8WAh8KaGRkAkMPDxYCHwpoZGQCRQ8WAh8JBQ1kaXNwbGF5Om5vbmU7FgJmD2QWBgIDDw9kFgIfBQUlaWYoIUNsaWNrQnRuQXBwcm92YWwoKSkgcmV0dXJuIGZhbHNlO2QCBQ8PZBYCHwkFDWRpc3BsYXk6bm9uZTtkAgsPD2QWAh8JBQ1kaXNwbGF5Om5vbmU7ZAJGDxYCHwkFDWRpc3BsYXk6bm9uZTsWAmYPZBYCAgMPD2QWBB8FBShpZighZm5fVmFsaWRhdGlvbl9Hcm91cCgpKSByZXR1cm4gZmFsc2U7HghkaXNhYmxlZAUEdHJ1ZWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFhQFFGN0bDAwJGlidG5Kb2luTXlQYWdlBRJjdGwwMCRpYnRuTG9nSW5PdXQFIWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkYnRuUHJldgUjY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpYnRuTG9naW4FLWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkcmRvQURpc2NvdW50SXNVc2UwMQUtY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRyZG9BRGlzY291bnRJc1VzZTAxBS1jdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJHJkb0FEaXNjb3VudElzVXNlMDIFMWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkY2hrQ29tcGFueURpc2NvdW50QWdyZWUFJ2N0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkYnRuUGFyZW50c0NoawUqY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRpYnRuSW5wdXRQYXhOYW1lBSFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJHJkb0NhcmQFIWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkcmRvQmFuawUhY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRyZG9CYW5rBSFjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJHJkb0tLQU8FIWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkcmRvS0tBTwUjY3RsMDAkQ29udGVudFBsYWNlSG9sZGVyMSRidG5QVUNhcmQFKGN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkYnRuUHJldkFwcHJvdmUFJWN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkaWJ0bkFwcHJvdmUFJmN0bDAwJENvbnRlbnRQbGFjZUhvbGRlcjEkYnRuUHJldkdyb3VwBSpjdGwwMCRDb250ZW50UGxhY2VIb2xkZXIxJGlidG5BcHByb3ZlR3JvdXB/H+XMzpY0ICRxhSQgy8br7YploA==">
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['aspnetForm'];
if (!theForm) {
    theForm = document.aspnetForm;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/WebResource.axd?d=7nqTy4RFwRl9jBxjXawsXh0smp4wXIRw88jbwOwgtr5Ok7-PaO9-2LPnQ91g0TaXYNFeKVYw7BgJGl_PVy4Zr8NVj6Q1&amp;t=635589759467565191" type="text/javascript"></script>


<script type="text/javascript">
//<![CDATA[
var vG_MasterPrefixID = 'ctl00_';
var vG_MasterPrefixName = 'ctl00$';
var vG_ContentPrefixID = 'ctl00_ContentPlaceHolder1_';
var vG_ContentPrefixName = 'ctl00$ContentPlaceHolder1$';
//]]>
</script>

<script src="/Script/json2.js" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[

function fn_Radio_Click(e, user_control_id ,flifo_code, std, etd) {
    var evt = window.event || e;
	var control = GetEventToggle(evt);
	if( control.tagName.toUpperCase() == "LABEL" ) {
        if(flifo_code != '' && flifo_code.indexOf('DLY') > -1) {
            alertFlag = '1';
        }
		control.children[0].click();
	}
	else if( control.tagName.toUpperCase() == "INPUT" ) {
		var seat_class = control.value;
		var fare = control.nextSibling.nodeValue;
		var cell = GetParent_by_Tag("TD", control);
		var flt_num = cell.parentNode.cells[0].innerHTML.replace(/(^\s*)|(\s*$)/gi, "");
        var dept_arrt = fn_GetCrossBrowsingInnerText(cell.parentNode.cells[2].innerHTML.replace(/(^\s*)|(\s*$)/gi, ""));
        var rev_cls = cell.children[0].value;
		var rule = cell.children[1].value;
		var remark = cell.children[2].value;
		fn_SetRule(user_control_id, flt_num, seat_class, fare, rev_cls, rule, remark, dept_arrt, evt )
        
        if(flifo_code != '' && flifo_code.indexOf('DLY') > -1) {
            if(alertFlag == '1'){   
                ShowDelayinfo(std, etd);
                alertFlag = '3';
            }
            else{
                if(alertFlag == '3'){
                    alertFlag = '2';
                }
                else{
                    alertFlag = '2';
                    ShowDelayinfo(std, etd);
                }
            }
        }
	}
}

function fn_SetRule(user_control_id, flt_num, seat_class, fare, rev_cls, rule, remark, dept_arrt, e ) {
    var rev_cls_desc = "";
	var rule_desc = "";
	var remark_desc = "";
	switch( rev_cls ) 
    {
		case "0" : 
		case "2" :
			switch( seat_class ) {
				case "G" : rev_cls_desc = "&nbsp;";  break;
                case "E" : rev_cls_desc = "&nbsp;출발 1시간전 최대 3회까지 가능합니다.";  break;
				default : rev_cls_desc = "&nbsp;출발 1시간전 최대 3회까지 가능합니다."; break;
			}
			break;
		default :
			switch( seat_class ) {
				case "G" : rev_cls_desc = "&nbsp;";  break;
				default : rev_cls_desc = "&nbsp;예약변경이 불가합니다."; break;
			}
			break;
	}
	switch( rule ) 
    {
		case "2" :
		case "3" : rule_desc = "&nbsp;환불이 불가합니다."; break;
		default :
			switch( seat_class ) {
				case "Y" :
					rule_desc = "<table width='98%' align='right' border='0' cellpadding='0' cellspacing='0'>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발60일전</br>~출발31일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 1천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발30일전~출발8일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 2천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발7일전~출발2일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 3천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발1일전~출발시간</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 8천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발 예정시간 이후</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 1만 2천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;' colspan='2'><font color='red'>(최초 예매 당일에는 위약금이 면제 됩니다.)</font></td></tr>";
                    rule_desc += "</table>";
					break;
				case "E" :
					rule_desc = "<table width='98%' align='right' border='0' cellpadding='0' cellspacing='0'>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발60일전</br>~출발31일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 1천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발30일전~출발8일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 2천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발7일전~출발2일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 3천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발1일전~출발시간</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 8천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발 예정시간 이후</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 1만 2천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;' colspan='2'><font color='red'>(최초 예매 당일에는 위약금이 면제 됩니다.)</font></td></tr>";
                    rule_desc += "</table>";
					break;
				case "G" :
					rule_desc = "<table width='98%' align='right' border='0' cellpadding='0' cellspacing='0'>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발60일전</br>~출발31일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 1천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발30일전~출발8일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 2천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발7일전~출발2일전</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 3천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발1일전~출발시간</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 8천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;'><font color='red'>출발 예정시간 이후</font></td><td style='font-size:11px;'><font color='red'>편도 1인당 1만 2천원</font></td></tr>";
                    rule_desc += "<tr><td style='font-size:11px;' colspan='2'><font color='red'>(최초 예매 당일에는 위약금이 면제 됩니다.)</font></td></tr>";
                    rule_desc += "</table>";
					break;
			}
			//rule_desc = "";
			break;
	}
	switch( remark ) { //안내사항
		case "00" : remark_desc = "&nbsp;"; break;
		default : remark_desc = "&nbsp;" + remark; break;
	}
	var rowCnt = Number( GetObj( user_control_id + "_hdnRowCount" ).value );
	var flight_discussion = "";
	if( rowCnt == null || rowCnt <= 0 )
		flight_discussion = "운항하는 항공편이 없습니다.";
	else if( flt_num == null || flt_num == "" )
		flight_discussion = "선택한 요금정보가 없습니다.";
	else if( seat_class == "Y" )
		flight_discussion = "편 일반운임 규정";
	else if( seat_class == "E" )
		flight_discussion = "편 할인운임 규정";
	else if( seat_class == "G" )
		flight_discussion = "편 단체운임 규정";
	else
		flight_discussion = "편 운임 규정";

	GetObj( user_control_id + "_hdnFare" ).value = fn_DeleteComma( fn_Trim(fare).replace("원", "") );
	GetObj( user_control_id + "_hdnBookingClass" ).value = seat_class;
	GetObj( user_control_id + "_hdnFLT_NUM" ).value = flt_num;
	GetObj( user_control_id + "_hdnDEPT_ARRT" ).value = dept_arrt;
	GetObj( user_control_id + "_hdnRule" ).value = rule;
	GetObj( user_control_id + "_lblFLT_NUM" ).innerHTML = flt_num;
	GetObj( user_control_id + "_lblFLT_Discussion" ).innerHTML = flight_discussion;
	GetObj( user_control_id + "_lblREV_CLS" ).innerHTML = rev_cls_desc;
	GetObj( user_control_id + "_lblRULE" ).innerHTML = rule_desc;
//	GetObj( user_control_id + "_lblREMARK" ).innerHTML = remark_desc;
	try {
		if(fn_SetSummaryText != null)
			fn_SetSummaryText(e, user_control_id);    //총 지불금액 계산
	}
	catch(e) {
		if( e.name != "TypeError" ) throw e;
	}
}

function SetFlightTable( user_control_id, e ) {
	var radioButtons = document.getElementsByName( "rdo" + user_control_id );
	var selectedFlt = GetObj( user_control_id + "_hdnFLT_NUM" ).value;
	var seat_class = GetObj( user_control_id + "_hdnBookingClass" ).value;
	var selected = false;
	var isempty = (IsEmpty(selectedFlt) || IsEmpty(seat_class));
	for(var i = 0; i < radioButtons.length; i++ ) {
		if( isempty == false ) {
			if( radioButtons[i].style["display"] != "none" && radioButtons[i].value == seat_class && GetParent_by_Tag( "TR", radioButtons[i] ).cells[0].innerHTML.replace(/(^\s*)|(\s*$)/gi, "") == selectedFlt ) {
                alertFlag = '3';
        		radioButtons[i].click();
                selected = true;
				seat_class = radioButtons[i].value;
				break;
			}
			else {
				continue;
			}
		}
		if( radioButtons[i].style["display"] != "none" && radioButtons[i].disabled != true && radioButtons[i].value != "E" ) {
            alertFlag = '3';
        	radioButtons[i].click();
            selected = true;
			seat_class = radioButtons[i].value;
			break;
		}
	}
	if( seat_class != "Y" && !selected ) {
		for(var i = 0; i < radioButtons.length; i++ ) {
			if( radioButtons[i].style["display"] != "none" && radioButtons[i].disabled != true ) {
                alertFlag = '3';
        		radioButtons[i].click();
				selected = true;
				seat_class = radioButtons[i].value;
				break;
			}
		}
	}
	if( !selected ) {
		for(var i = 0; i < radioButtons.length; i++ ) {
			if( radioButtons[i].style["display"] != "none" && radioButtons[i].disabled != true ) {
                alertFlag = '3';
        		radioButtons[i].click();
				selected = true;
				seat_class = radioButtons[i].value;
				break;
			}
		}
	}
	if( !selected && GetObj(user_control_id + "_hdnFormerFareYN").value != "Y") {
		GetObj( user_control_id + "_hdnFLT_NUM" ).value = "";
		GetObj( user_control_id + "_hdnBookingClass" ).value = "";
		GetObj( user_control_id + "_lblFLT_NUM" ).innerHTML = "";
		var rowCnt = Number( GetObj( user_control_id + "_hdnRowCount" ).value );
		var flight_discussion = "";
		if( rowCnt == null || rowCnt <= 0 )
			flight_discussion = "운항하는 항공편이 없습니다.";
		else
			flight_discussion = "선택한 요금정보가 없습니다.";
		GetObj( user_control_id + "_lblFLT_Discussion" ).innerHTML = flight_discussion;
		try {
			if(fn_SetSummaryText != null)
				fn_SetSummaryText();
		}
		catch(e) {
			if( e.name != "TypeError" ) throw e;
		}
	}
	else if( !selected && !isempty ) {
		var fare = GetObj( user_control_id + "_hdnFare" ).value;
		var rule = GetObj( user_control_id + "_hdnRule" ).value;
		var remark = GetObj( user_control_id + "_lblREMARK" ).innerHTML;
		var dept_arrt = GetObj( user_control_id + "_hdnDEPT_ARRT" ).value;
		fn_SetRule( user_control_id, selectedFlt, seat_class, fare, rule, rule, remark, dept_arrt, e );
	}
}

function fn_SetFlightTable_Height() {
	var trTemp = document.getElementsByName("trTemp");
	if( trTemp.length == 2 ) {
		trTemp[0].style.height = "10px";
		trTemp[1].style.height = "10px";
		var tbl_Left = GetParent_by_Tag("TABLE", trTemp[0]);
		var tbl_Right = GetParent_by_Tag("TABLE", trTemp[1]);
		var gap = 10;
		if( tbl_Left.offsetHeight > tbl_Right.offsetHeight ) {
			gap += tbl_Left.offsetHeight - tbl_Right.offsetHeight;
			trTemp[1].style.height = gap.toString() + "px";
		}
		else {
			gap += tbl_Right.offsetHeight - tbl_Left.offsetHeight;
			trTemp[0].style.height = gap.toString() + "px";
		}
	}
}

function fn_FlightTable_Visible( user_control_id ) {
	var visible = GetObj( user_control_id + "_hdnVisible" ).value;
	var tblFlight = GetObj( user_control_id + "_tblFlight" );
	var imgTemp = GetObj( user_control_id + "_imgTemp" );
	if( visible == "false" ) {
		tblFlight.style.display = "none";
		imgTemp.style.display = "inline";
		var p_tbl = GetParent_by_Tag("TABLE", imgTemp);
		var p_row = GetParent_by_Tag("TR", p_tbl);
		p_tbl.style.height = p_row.offsetHeight;
	}
	else {
		tblFlight.style.display = "inline";
		imgTemp.style.display = "none";
	}
}

function fn_GetFare(user_control_id, e)
{
    try
    {
        SetFlightTable(user_control_id, e);
    }
    catch(e)
    {
        alert(e);
    }
    return false;
}
var __cultureInfo = '{"name":"ko-KR","numberFormat":{"CurrencyDecimalDigits":0,"CurrencyDecimalSeparator":".","IsReadOnly":true,"CurrencyGroupSizes":[3],"NumberGroupSizes":[3],"PercentGroupSizes":[3],"CurrencyGroupSeparator":",","CurrencySymbol":"₩","NaNSymbol":"NaN","CurrencyNegativePattern":1,"NumberNegativePattern":1,"PercentPositivePattern":0,"PercentNegativePattern":0,"NegativeInfinitySymbol":"-Infinity","NegativeSign":"-","NumberDecimalDigits":2,"NumberDecimalSeparator":".","NumberGroupSeparator":",","CurrencyPositivePattern":0,"PositiveInfinitySymbol":"Infinity","PositiveSign":"+","PercentDecimalDigits":2,"PercentDecimalSeparator":".","PercentGroupSeparator":",","PercentSymbol":"%","PerMilleSymbol":"‰","NativeDigits":["0","1","2","3","4","5","6","7","8","9"],"DigitSubstitution":1},"dateTimeFormat":{"AMDesignator":"오전","Calendar":{"MinSupportedDateTime":"\/Date(-62135596800000)\/","MaxSupportedDateTime":"\/Date(253402268399999)\/","AlgorithmType":1,"CalendarType":1,"Eras":[1],"TwoDigitYearMax":2029,"IsReadOnly":true},"DateSeparator":"-","FirstDayOfWeek":0,"CalendarWeekRule":0,"FullDateTimePattern":"yyyy\u0027년\u0027 M\u0027월\u0027 d\u0027일\u0027 dddd tt h:mm:ss","LongDatePattern":"yyyy\u0027년\u0027 M\u0027월\u0027 d\u0027일\u0027 dddd","LongTimePattern":"tt h:mm:ss","MonthDayPattern":"M\u0027월\u0027 d\u0027일\u0027","PMDesignator":"오후","RFC1123Pattern":"ddd, dd MMM yyyy HH\u0027:\u0027mm\u0027:\u0027ss \u0027GMT\u0027","ShortDatePattern":"yyyy-MM-dd","ShortTimePattern":"tt h:mm","SortableDateTimePattern":"yyyy\u0027-\u0027MM\u0027-\u0027dd\u0027T\u0027HH\u0027:\u0027mm\u0027:\u0027ss","TimeSeparator":":","UniversalSortableDateTimePattern":"yyyy\u0027-\u0027MM\u0027-\u0027dd HH\u0027:\u0027mm\u0027:\u0027ss\u0027Z\u0027","YearMonthPattern":"yyyy\u0027년\u0027 M\u0027월\u0027","AbbreviatedDayNames":["일","월","화","수","목","금","토"],"ShortestDayNames":["일","월","화","수","목","금","토"],"DayNames":["일요일","월요일","화요일","수요일","목요일","금요일","토요일"],"AbbreviatedMonthNames":["1","2","3","4","5","6","7","8","9","10","11","12",""],"MonthNames":["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월",""],"IsReadOnly":true,"NativeCalendarName":"서기 (한글)","AbbreviatedMonthGenitiveNames":["1","2","3","4","5","6","7","8","9","10","11","12",""],"MonthGenitiveNames":["1월","2월","3월","4월","5월","6월","7월","8월","9월","10월","11월","12월",""]}}';//]]>
</script>

<script src="../Script/AjaxTookit/System.Web.Extensions/1.0.61025.0/MicrosoftAjax.js" type="text/javascript"></script>
<script src="../Script/AjaxTookit/System.Web.Extensions/1.0.61025.0/MicrosoftAjaxWebForms.js" type="text/javascript"></script>
<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="1479AD23">
</div>
        <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('ctl00$ScriptManager1', document.getElementById('aspnetForm'));
Sys.WebForms.PageRequestManager.getInstance()._updateControls([], [], [], 600);
//]]>
</script>

        <script type="text/javascript">
            function SelectLanguage(language) {
                __doPostBack("ctl00$btnChangeLanguage", language);
            }
        </script>
        <div id="wrapper" style="z-index: 999;">
            <div id="skipMenu">
                <a href="javascript:SkipMenu();">본문 바로가기</a>
            </div>
            <div id="header">
                <h1><a href="/Default.aspx">
                    <img src="/images/newMain/top_logo_2014.gif" alt="JIN AIR"></a></h1>
                <div class="utilCont">
                    <ul>
                        <li class="first"><a href="/Default.aspx">
                            <img src="/images/newMain/top_home.gif" alt="홈"></a></li>
                        <li><a href="/HOM/FAQ/FAQ01List.aspx">
                            <img src="/images/newMain/top_customer.gif" alt="고객서비스센터"></a></li>
                        <li>
                            <input type="image" name="ctl00$ibtnJoinMyPage" id="ctl00_ibtnJoinMyPage" src="/images/newMain/top_join.gif" alt="회원가입" style="border-width:0px;">
                        </li>
                        <li>
                            <input type="image" name="ctl00$ibtnLogInOut" id="ctl00_ibtnLogInOut" src="/images/newMain/top_login.gif" alt="로그인" style="border-width:0px;">
                        </li>

                        <li class="boxShow"><a href="javascript:void(0);">
                            <img src="/images/newMain/language.gif" alt="LANGUAGE"></a>
                            <ul>
                                <li><a href="javascript:SelectLanguage('ENG|USD')">
                                    <img src="/images/newMain/language_select1.png" alt="ENGLISH"></a></li>
                                <li><a href="javascript:SelectLanguage('CHN|USD')">
                                    <img src="/images/newMain/language_select2.png" alt="简体"></a></li>
                                <li><a href="javascript:SelectLanguage('CHT|USD')">
                                    <img src="/images/newMain/language_select3.png" alt="繁體"></a></li>
                                <li><a href="javascript:SelectLanguage('JPN|USD')">
                                    <img src="/images/newMain/language_select4.png" alt="日本語"></a></li>
                            </ul>
                        </li>
                        <li><a href="/HOM/SiteMap/SiteMap.aspx">
                            <img src="/images/newMain/top_sitemap.gif" alt="사이트맵"></a></li>
                    </ul>
                    <div id="welcome">
                        <span class="Mbookinput">
                            <span id="ctl00_lblUserName"></span>
                            <span id="ctl00_lblRemainPoint"></span>
                        </span>
                    </div>
                </div>
                <ul id="gnb">
                    <li><a href="/bookflight/flightSearch.aspx">
                        <img src="/images/newMain/menu1_off.gif" alt="항공권 예매"></a>
                        <ul>
                            <li><a href="/RSV/RSV_ScheduleSelect.aspx">
                                <img src="/images/newMain/gnb_sub1_1_off_new.gif" alt="국내선 예매"></a></li>
                            <li><a href="/bookflight/flightSearch.aspx">
                                <img src="/images/newMain/gnb_sub1_2_off_new.gif" alt="국제선 예매"></a></li>
                            <li><a href="/RSVInternational/ReservationList.aspx">
                                <img src="/images/newMain/gnb_sub1_4_off_new.gif" alt="예약조회/변경/환불"></a></li>
                            <li><a href="/RSV/DiscountInfo.aspx">
                                <img src="/images/newMain/gnb_sub1_5_off_new.gif" alt="할인제도"></a></li>
                        </ul>
                    </li>
                    <li><a href="/RSVInternational/FlightInfo.aspx">
                        <img src="/images/newMain/menu2_off.gif" alt="운항 정보"></a>
                        <ul>
                            <li><a href="/RSVInternational/FlightInfo.aspx">
                                <img src="/images/newMain/gnb_sub2_1_off_new.gif" alt="출도착 조회"></a></li>
                            <li><a href="/RSVInternational/ScheduleList.aspx">
                                <img src="/images/newMain/gnb_sub2_2_off_new.gif" alt="스케줄 조회"></a></li>
                            <li><a href="/HOM/Operate/RouteMap.aspx">
                                <img src="/images/newMain/gnb_sub2_3_off_new.gif" alt="취항노선 안내"></a></li>
                        </ul>
                    </li>
                    <li><a href="/HOM/Service/Reservation.aspx">
                        <img src="/images/newMain/menu3_off.gif" alt="서비스 안내"></a>
                        <ul>
                            <li><a href="/HOM/Service/Reservation.aspx">
                                <img src="/images/newMain/gnb_sub3_1_off_new.gif" alt="예매 서비스"></a></li>
                            <li><a href="/HOM/Service/AirportCounter_01.aspx">
                                <img src="/images/newMain/gnb_sub3_2_off_new.gif" alt="공항 서비스"></a></li>
                            <li><a href="/HOM/Service/Drink.aspx">
                                <img src="/images/newMain/gnb_sub3_3_off_new.gif" alt="기내 서비스"></a></li>
                            <li><a href="/HOM/Service/AdditionalSevice.aspx">
                                <img src="/images/newMain/gnb_sub3_4_off_new.gif" alt="부가서비스"></a></li>
                            <li><a href="/HOM/Service/CargoTR.aspx">
                                <img src="/images/newMain/gnb_sub3_5_off_new.gif" alt="화물 운송"></a></li>
                            <li><a href="/HOM/Service/PointCoupon.aspx">
                                <img src="/images/newMain/gnb_sub3_6_off_new.gif" alt="지니 쿠폰"></a></li>
                        </ul>
                    </li>
                    <li><a href="/HOM/NaviPoint/PointInfo.aspx">
                        <img src="/images/newMain/menu4_off.gif" alt="나비포인트"></a>
                        <ul>
                            <li><a href="/HOM/NaviPoint/PointInfo.aspx">
                                <img src="/images/newMain/gnb_sub4_1_off_new.gif" alt="나비포인트 안내"></a></li>
                            <li><a href="/HOM/NaviPoint/PointMain.aspx">
                                <img src="/images/newMain/gnb_sub4_2_off_new.gif" alt="나비포인트 적립/조회"></a></li>
                            <li><a href="/HOM/NaviPoint/BonusTicket.aspx">
                                <img src="/images/newMain/gnb_sub4_3_off_new.gif" alt="보너스항공권"></a></li>
                            <li><a href="/HOM/NaviPoint/SavingStandard.aspx">
                                <img src="/images/newMain/gnb_sub4_4_off_new.gif" alt="포인트 적립/사용 기준"></a></li>
                        </ul>
                    </li>
                    <li><a href="/HOM/TRService/AirTelMain.aspx">
                        <img src="/images/newMain/menu5_off.gif" alt="지니몰"></a>
                        <ul>
                            <li><a href="/HOM/TRService/AirTelMain.aspx">
                                <img src="/images/newMain/gnb_sub5_1_off_new.gif" alt="지니텔"></a></li>
                            <li><a href="/HOM/TRService/JiniPassJeju.aspx">
                                <img src="/images/newMain/gnb_sub5_2_off_new.gif" alt="지니 패스"></a></li>
                            <li><a href="/HOM/TRService/Insurance.aspx">
                                <img src="/images/newMain/gnb_sub5_3_off_new.gif" alt="여행자보험"></a></li>
                            <li><a href="/HOM/TRService/rentacar_default.aspx">
                                <img src="/images/newMain/gnb_sub5_4_off_new.gif" alt="렌터카"></a></li>
                            
                            
                            <li><a href="javascript:void(0);" onclick="window.open('http://www.booking.com/index.ko.html?aid=393155&amp;label=topnavitap', '_blank', 'resizable=1, scrollbars=1, top=50, left=250, width=1050, height=650');">
                                <img src="/images/newMain/gnb_sub5_5_off_new.gif" alt="호텔"></a></li>
                            <li><a href="/HOM/TRService/JinShop.aspx">
                                <img src="/images/newMain/gnb_sub5_6_off_new.gif" alt="진에어숍"></a></li>
                            <li class="lastLi5"><a href="/HOM/TRService/Hanjin.aspx">
                                <img src="/images/newMain/gnb_sub5_7_off_new.gif" alt="택배"></a></li>
                        </ul>
                    </li>
                    <li><a href="/HOM/Company/Ceo.aspx">
                        <img src="/images/newMain/menu6_off.gif" alt="회사소개"></a>
                        <ul>
                            <li><a href="/HOM/Company/Ceo.aspx">
                                <img src="/images/newMain/gnb_sub6_1_off_new.gif" alt="일반현황"></a></li>
                            <li><a href="/HOM/company/office.aspx">
                                <img src="/images/newMain/gnb_sub6_2_off_new.gif" alt="지점안내"></a></li>
                            <li><a href="/HOM/Company/Airplane.aspx">
                                <img src="/images/newMain/gnb_sub6_3_off_new.gif" alt="기종소개"></a></li>
                            <li><a href="/HOM/Notice/NoticeList.aspx">
                                <img src="/images/newMain/gnb_sub6_4_off_new.gif" alt="홍보센터"></a></li>
                            <li><a href="/HOM/Event/Event01List.aspx">
                                <img src="/images/newMain/gnb_sub6_5_off_new.gif" alt="이벤트"></a></li>
                            <li><a href="/HOM/PRCenter/JiniLetter\JiniInsight.aspx">
                                <img src="/images/newMain/gnb_sub6_7_off.gif" alt="지니인사이트"></a></li>
                        </ul>
                    </li>
                </ul>
            </div>
        </div>
        <div id="content_sub" align="center">
            <table width="900px" border="0" cellpadding="0" cellspacing="0">
                <tbody><tr>
                    <td width="175px" height="100%" valign="top">
                        <table width="175px" height="100%" border="0" cellpadrding="0" cellspacing="0">
                            <tbody><tr>
                                <td>
                                    <div id="ctl00_pnlLeftMenu" style="height:100%;">
	
                                    
<div id="nav">
    <h2>
        <img id="ctl00_ctl12_imgTitle" src="/images/left_menu/Book_left_tit.gif" alt="항공권 예매" style="border-width:0px;">
    </h2>
    <ul>
        <li>
            <a href="/RSV/RSV_ScheduleSelect.aspx">
                <img id="ctl00_ctl12_btnMenu1110" onmouseout="this.src='/images/left_menu/Book_menu1_up.gif'" onmouseover="this.src='/images/left_menu/Book_menu1_up.gif'" src="/images/left_menu/Book_menu1_up.gif" alt="국내선 예매" style="border-width:0px;">
            </a>
            
        </li>
        <li>
            <a href="/BookFlight/FlightSearch.aspx">
                <img id="ctl00_ctl12_btnMenu1120" onmouseout="this.src='/images/left_menu/Book_menu2.gif'" onmouseover="this.src='/images/left_menu/Book_menu2_up.gif'" src="/images/left_menu/Book_menu2.gif" alt="국제선 예매" style="border-width:0px;">
            </a>
            
        </li>
        <li>
            <a href="/RSVInternational/ReservationList.aspx">
                <img id="ctl00_ctl12_btnMenu1140" onmouseout="this.src='/images/left_menu/Book_menu4.gif'" onmouseover="this.src='/images/left_menu/Book_menu4_up.gif'" src="/images/left_menu/Book_menu4.gif" alt="예약조회/변경/환불" style="border-width:0px;">
            </a>
            
        </li>
        <li>
            <a href="/RSV/DiscountInfo.aspx">
                <img id="ctl00_ctl12_btnMenu1150" onmouseout="this.src='/images/left_menu/Book_menu5.gif'" onmouseover="this.src='/images/left_menu/Book_menu5_up.gif'" src="/images/left_menu/Book_menu5.gif" alt="할인제도" style="border-width:0px;">
            </a>
        </li>
        <li class="cs">
            <a href="/HOM/FAQ/FAQ01List.aspx">
                <img id="ctl00_ctl12_imgFaq" src="/images/left_menu/Left_menu_faq.gif" alt="FAQ 자주묻는 질문" style="border-width:0px;">
            </a>
        </li>
        <li>
            <a href="/HOM/FAQ/MailReqWrite.aspx">
                <img id="ctl00_ctl12_imgQnA" src="/images/left_menu/Left_menu_qna.gif" alt="Q&amp;A 1:1 고객문의" style="border-width:0px;">
            </a>
        </li>
    </ul>
    <br>
    
    
    <a href="javascript:void(0);" onclick="window.open('http://www.booking.com/index.ko.html?aid=393155&amp;label=HpKrSub', '_blank', 'resizable=1, scrollbars=1, top=50, left=250, width=1050, height=650');">
        <img id="ctl00_ctl12_imgBookingCom" src="/images/left_menu/banner_booking.gif" alt="호텔 특가를 한눈에, Booking.com" style="border-width:0px;">
    </a>
    <br>
    
    
    <a href="javascript:void(0);" onclick="window.open('http://www.rentalcars.com/?affiliateCode=jinair&amp;adplat=subbanner&amp;preflang=ko', '_blank', 'resizable=1, scrollbars=1, top=0, left=0, width=1024, height=768');">
        <img id="ctl00_ctl12_imgRentalcars" src="/images/left_menu/banner_rentalcars.gif" alt="최저가 렌터카 예약은 Rentalcars.com (새창열림)" style="border-width:0px;">
    </a>
</div>

</div>
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                    <td width="10px"></td>
                    <td width="715px" align="center" valign="top" background="/images/body_line02.gif" id="content_tbl">
                        
    <script type="text/javascript">
        var currLang = "KOR"; // 현재 언어
    </script>
    <script src="/Script/json2.js"></script>

    <script type="text/javascript">
        var payFormName = "aspnetForm";
    </script>

    <script type="text/javascript" src="/Script/ReservationPurchase.js"></script>

    
    <script src="/Script/DomesticReservation.js"></script>
    <script type="text/javascript">

        //결제방법 선택에 따른 분기
        function goPurchase() {
            if (GetObj("ctl00_ContentPlaceHolder1_rdoCard").checked) {
                // goIntoGate();
                f_card();
            }
            else if (GetObj("ctl00_ContentPlaceHolder1_rdoPrivateCard").checked) {
                goPrivateCardGate();
            }
            else if (GetObj("ctl00_ContentPlaceHolder1_rdoBank").checked) {
                goBankPayGate();
            }
            else if (GetObj("ctl00_ContentPlaceHolder1_rdoCash").checked) {
                ProgressBar("purchase");
                GetObj("btnCashConfirm").click();
            }
            else if (GetObj("ctl00_ContentPlaceHolder1_rdoKKAO").checked) {
                ProgressBar("purchase");
                OpenKakaoPopup();
            }
            else {
                alert('구매방법을 선택해 주세요');
                return false;
            }
}

function goPrivateCardGate() {
    try {
        //setTimeout("ProgressBar('purchase')","50");   //ProgressBar(100)
        ProgressBar('purchase');
        __doPostBack('ctl00$ContentPlaceHolder1$btnPrivateCardConfirm','');
        RemoveProgressBar();    //Remove ProgressBar
    }
    catch (e) {
        RemoveProgressBar();    //Remove ProgressBar
    }
}

function goBankPayGate() {
    try {
        //setTimeout("ProgressBar('purchase')","50");   //ProgressBar(100)
        ProgressBar('purchase');
        if (payRequest(bankRequestForm)) {
            SetBankPayData();

            __doPostBack('ctl00$ContentPlaceHolder1$btnBankPayConfirm','');
        }
        else {
            CancelApproval();
            alert("지불에 실패하였습니다.");
            fn_SetSummaryText();    //구매 시도후 실패한 경운 운임정보를 다시 가져와야 함
            bankRequestForm.reset();
        }
        RemoveProgressBar();    //Remove ProgressBar
    }
    catch (e) {
        CancelApproval();
        fn_SetSummaryText();    //구매 시도후 실패한 경운 운임정보를 다시 가져와야 함
        RemoveProgressBar();    //Remove ProgressBar
    }
}

function goIntoGate() {
    GetObj("EP_user_mail").value = GetObj("ctl00_ContentPlaceHolder1_txtEmail").value;

    //한글이 들어가는 값은 모두 encoding 필수.
    frm_pay.EP_mall_nm.value = encodeURIComponent(frm_pay.EP_mall_nm.value);
    frm_pay.EP_product_nm.value = encodeURIComponent(frm_pay.EP_product_nm.value);

    frm_pay.product_type.value = "0";

    //팝업 생성 후 부모창 수정 불가
    ProgressBar('purchase');

    var screenWidth = window.screen.availWidth;
    var screenHeight = window.screen.availHeight;

    var top = (screenHeight - 546 - 20) / 2;
    var left = (screenWidth - 816) / 2;

    //결제 팝업 생성
    var webPay = window.open("/Common/WebpayReq.aspx", "kicc_webpay", "width=816, height=546, innerWidth=823, innerHeight=500, location=no, menubar=no, resizable=no, scrollbars=no, status=no, toolbar=no,top=" + top + " ,left=" + left);

    //팝업 창 닫힘 확인 interval
    var interval = window.setInterval(function () {
        try {
            if (webPay == null || webPay.closed) {
                window.clearInterval(interval);
                if (frm_pay.EP_res_cd.value == "0000")
                    WebpaySuccess();
                else
                    WebpayFail();
            }
        }
        catch (e) {
            WebpayFail();
        }
    }, 100);
}

function f_card() {
    var frm_pay = document.frm_pay;
    //frm_pay.user_mail.value = GetObj("<= this.txtEmail.ClientID %>").value;
    frm_pay.EP_card_cd.value = GetObj("ddl_card_cd").value;

    /*  주문정보 확인 */
    if (!frm_pay.EP_card_cd.value) {
        alert("신용카드를 선택하세요.!!");
        frm_pay.EP_card_cd.focus();
        return;
    }
    ProgressBar('purchase');

    if (frm_pay.EP_product_amt.value < 50000) {
        frm_pay.EP_install_period.value = "00";
        frm_pay.EP_noint_yn.value = "N";
    }
    else {
        frm_pay.EP_install_period.value = GetObj("ddl_install_period").value;//frm_pay.install_period.value;
    }

    /* UTF-8 사용가맹점의 경우 EP_charset 값 셋팅 필수 */
    if (frm_pay.EP_charset.value == "UTF-8") {
        // 한글이 들어가는 값은 모두 encoding 필수.
        frm_pay.EP_mall_nm.value = encodeURIComponent(frm_pay.EP_mall_nm.value);
        frm_pay.EP_product_nm.value = encodeURIComponent(frm_pay.EP_product_nm.value);
        frm_pay.user_addr.value = encodeURIComponent(frm_pay.user_addr.value);
        frm_pay.user_nm.value = encodeURIComponent(frm_pay.user_nm.value);
    }

    var popW;
    var popH;
    var codeCd = GetObj("ddl_card_cd").value;
    if (codeCd == "031") { /**삼성카드 MPI **/
        popW = 410;
        popH = 500;
    }
    else if (codeCd == "027") { /**현대카드 MPI **/
        popW = 390;
        popH = 480;
    }
    else if (codeCd == "047") { /**롯데카드 MPI **/
        popW = 650;
        popH = 490;
    }
    else if (codeCd == "029") { /**신한카드 MPI **/
        popW = 400;
        popH = 480;
    }
    else if (codeCd == "008") { /**하나(외환) MPI **/
        popW = 620;
        popH = 500;
    }
    else if (codeCd == "018") { /**NH농협 MPI **/
        popW = 440;
        popH = 600;
    }
    else if (codeCd == "006") { /**하나카드 MPI **/
        popW = 630;
        popH = 460;
    }
    else if (codeCd == "022") { /**씨티카드 MPI**/
        popW = 680;
        popH = 480;
    }
    else if (codeCd == "050") { /**비자**/
        popW = 620;
        popH = 460;
    }
    else if (codeCd == "049") { /**마스터**/
        popW = 620;
        popH = 460;
    }
    else if (codeCd == "028") { /**JCB**/
        popW = 620;
        popH = 460;
    } else {
        popW = 600;
        popH = 500;
    }
    var popOpt = "height=" + popH + ", width=" + popW + ", dependent=yes, status=no, minimizable=no, fullscreen=no, location=no, scrollbars=no, menubar=no, toolbar=no, titlebar=no, directories=no, resizable=no";
    var webPay = window.open("", "hiddenifr", popOpt);
    frm_pay.target = "hiddenifr";
    frm_pay.action = "/Easypay/card_req.aspx";
    frm_pay.submit();

    //팝업 창 닫힘 확인 interval
    var interval = window.setInterval(function () {
        try {
            if (webPay == null || webPay.closed) {
                window.clearInterval(interval);

                if (frm_pay.EP_res_cd.value != "0000")
                    WebpayFail();
            }
        }
        catch (e) {
            WebpayFail();
        }
    }, 100);
}

function f_submit() {
    var frm_pay = document.frm_pay;

    GetObj("ctl00_ContentPlaceHolder1_hdnEvReqType").value = GetObj("EP_req_type").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvCardAmt").value = GetObj("EP_card_amt").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvInstallPeriod").value = GetObj("EP_install_period").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvCavv").value = GetObj("EP_cavv").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvXid").value = GetObj("EP_xid").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvEci").value = GetObj("EP_eci").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvKvpCardcode").value = GetObj("EP_kvp_cardcode").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvKvpSessionKey").value = GetObj("EP_kvp_sessionkey").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvKvpEcnData").value = GetObj("EP_kvp_encdata").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnEvKvpPgid").value = GetObj("EP_kvp_pgid").value;

    if (GetObj("EP_req_type").value == "0" && GetObj("EP_card_no").value.length > 16) {
        GetObj("ctl00_ContentPlaceHolder1_hdnEvExpireDate").value = "8911";
        GetObj("ctl00_ContentPlaceHolder1_hdnEvCardNo").value = GetObj("EP_card_no").value.substring(0, 16);
    }
    else {
        GetObj("ctl00_ContentPlaceHolder1_hdnEvCardNo").value = GetObj("EP_card_no").value;
    }

    // 정상("0000") 일 때 승인요청페이지로 이동.
    if (frm_pay.EP_res_cd.value == "0000") {
        if (frm_pay.EP_charset.value == "UTF-8") {
            // 한글이 들어가는 값은 모두 encoding 필수.
            frm_pay.EP_mall_nm.value = decodeURIComponent(frm_pay.EP_mall_nm.value);
            frm_pay.EP_product_nm.value = decodeURIComponent(frm_pay.EP_product_nm.value);
            frm_pay.user_addr.value = decodeURIComponent(frm_pay.user_addr.value);
            frm_pay.user_nm.value = decodeURIComponent(frm_pay.user_nm.value);

        }
        fn_Enable_Change(GetObj("ibtnApprove"), false);
        __doPostBack('ctl00$ContentPlaceHolder1$btnConfirm','');
    }
    else {
        WebpayFail()
    }
    RemoveProgressBar();
}

function WebpayFail() {
    //인증취소, 실패
    CancelApproval();
    alert("지불에 실패하였습니다.");
    fn_SetSummaryText();    //구매 시도후 실패한 경운 운임정보를 다시 가져와야 함		        
    RemoveProgressBar();    //Remove ProgressBar
    fn_Enable_Change(GetObj("ibtnApprove"), true);
}

//카카오페이 팝업 open
function OpenKakaoPopup() {
    KKAOPopup("/KakaoPay/PaymentProcess.aspx", "KakaoPay", "435", "560", "no");
}

//카카오페이 인증 후 승인
function goKakaoPay() {
    GetObj("ctl00_ContentPlaceHolder1_hdnKKAOAmt").value = GetObj("Amt").value;
    var paxFamilyName = GetObj("ctl00_ContentPlaceHolder1_rptPassengerList_ctl01_txtFamilyName").value;
    var paxGivenName = GetObj("ctl00_ContentPlaceHolder1_rptPassengerList_ctl01_txtGivenName").value;
    GetObj("ctl00_ContentPlaceHolder1_hdnBuyerName").value = paxFamilyName + paxGivenName;
    GetObj("ctl00_ContentPlaceHolder1_hdnPayParams").value = GetObj("KakaoAuthResult").value;
    __doPostBack('ctl00$ContentPlaceHolder1$btnKakaoConfirm','');
    RemoveProgressBar();
}

//카카오페이 팝업창 닫기 처리
var KKAOPopup = function (uri, title, width, height, scrollbars) {
    var win = fn_OpenWindow(uri, title, width, height, scrollbars);
    var interval = window.setInterval(function () {
        try {
            if (win == null || win.closed) {
                window.clearInterval(interval);
                RemoveProgressBar();
                if (GetObj("KakaoAuthResult").value == "") {
                    CancelApproval();
                    alert("지불에 실패하였습니다.");
                }
            }
        }
        catch (e) {
        }
    }, 100);
    return win;
}

function CancelApproval() {
    //인증실패할 경우 pnr삭제(paxseg삭제, pnr미삭제) - 2014.07.21 김태우
    if (GetObj("hdnPNR_NO").value.length > 0 && GetObj("hdnComplete").value != "Y") {
        RequestHTTP("<REQUEST><TASK>CancelsApproval</TASK><PNR_NO>" + GetObj("hdnPNR_NO").value + "</PNR_NO></REQUEST>", null, document.location.protocol + "//" + document.location.host + "/RSV/RSV_WebResult.aspx");
    }
}

function SetBankPayData() {
    var bankPayData;
    bankPayData = GetObj("tx_bank_test").value + "|" + GetObj("hd_pre_msg_type").value + "|" + GetObj("hd_msg_code").value + "|" + GetObj("hd_msg_type").value + "|" + GetObj("hd_ep_type").value + "|" + GetObj("hd_pi").value + "|" + GetObj("hd_approve_no").value + "|" + GetObj("hd_serial_no").value + "|" + GetObj("hd_firm_name").value + "|" + GetObj("hd_input_option").value + "|" + GetObj("hd_ep_option").value + "|" + GetObj("tx_amount").value + "|" + GetObj("tx_user_define").value + "|" + GetObj("hd_timeout_yn").value + "|" + GetObj("hd_timeout").value + "|" + GetObj("tx_bill_yn").value + "|" + GetObj("tx_email_addr").value;
    GetObj("hidBankPay").value = bankPayData;
}
    </script>

    <script type="text/javascript" src="../Script/xmlHTTP.js"></script>

    <script type="text/javascript">

        var last_focus_fare;
        var checkedFare;
        function fn_SetSummaryText(e, fareListControl) {
            var Adult = Number(GetObj("hdnAdult").value);
            var Disable = Number(GetObj("hdnDisable").value);
            var DisableSub = Number(GetObj("hdnDisableSub").value);
            var Etc = Number(GetObj("hdnEtc").value);
            var Child = Number(GetObj("hdnChild").value);
            var Infant = Number(GetObj("hdnInfant").value);
            var req_seat_count = Adult + Child + Disable + DisableSub + Etc;

            var downline_flt_num = GetObj("fltlstDownLine_hdnFLT_NUM").value;
            var downline_class = GetObj("fltlstDownLine_hdnBookingClass").value;
            var downline_date = GetObj("fltlstDownLine_hdnDate").value;

            var upline_flt_num = GetObj("fltlstUpLine_hdnFLT_NUM").value;
            var upline_class = GetObj("fltlstUpLine_hdnBookingClass").value;
            var upline_date = GetObj("fltlstUpLine_hdnDate").value;
            var mbr_gb = GetObj("hdnGroupYN").value == "Y" ? "G" : "I";
            //var agent_cd = "";
            //대리점 예약 단계에서는 1차 운임과 동일한 운임이 나타나도록 처리
            var agent_cd = "";

            var evt;
            if (e != null)
                evt = GetEventToggle(e);

            if (evt != null && evt.tagName.toUpperCase() == "INPUT")
                last_focus_fare = evt;

            if (fareListControl != null)
                checkedFare = GetObj(fareListControl + "_hdnFare").value;

            var request_xml = "<REQUEST><TASK>Avail_FareClac</TASK>";
            request_xml += "<REQ_SEAT_CNT>" + req_seat_count.toString() + "</REQ_SEAT_CNT>";
            request_xml += "<DOWNLINE_FLT_NUM>" + downline_flt_num + "</DOWNLINE_FLT_NUM>";
            request_xml += "<UPLINE_FLT_NUM>" + upline_flt_num + "</UPLINE_FLT_NUM>";
            request_xml += "<DOWNLINE_CLASS>" + downline_class + "</DOWNLINE_CLASS>";
            request_xml += "<UPLINE_CLASS>" + upline_class + "</UPLINE_CLASS>";
            request_xml += "<DOWNLINE_DATE>" + downline_date + "</DOWNLINE_DATE>";
            request_xml += "<UPLINE_DATE>" + upline_date + "</UPLINE_DATE>";
            request_xml += "<DEPARTURE>" + GetObj("hdnDeparture").value + "</DEPARTURE>";
            request_xml += "<ARRIVAL>" + GetObj("hdnArrival").value + "</ARRIVAL>";
            request_xml += "<MBR_GB>" + mbr_gb + "</MBR_GB>";
            request_xml += "<AGENT_CD>" + agent_cd + "</AGENT_CD>";
            request_xml += "</REQUEST>";

            if (!IsEmpty(downline_flt_num + upline_flt_num + downline_class + upline_class)) {
                RequestHTTP(request_xml, ReceiveFareCalc);	//	Script/Common.js에 정의되어 있으며 사용법은 해당 주석을 참조한다.
            }
            else {
                var tdTotal_Exp = GetObj("tdTotal_Exp");
                var tdTotal_Amt = GetObj("tdTotal_Amt");
                var tdTotal_Inf = GetObj("tdTotal_Inf");
                tdTotal_Exp.innerHTML = " =";
                tdTotal_Amt.innerHTML = "0원";
                tdTotal_Inf.innerHTML = "&nbsp;";
                var tdTax_Exp = GetObj("tdTax_Exp");
                var tdTax_Amt = GetObj("tdTax_Amt");
                var tdTax_Inf = GetObj("tdTax_Inf");
                tdTax_Exp.innerHTML = " =";
                tdTax_Amt.innerHTML = "0원";
                tdTax_Inf.innerHTML = "&nbsp;";
                var tdFuel_Exp = GetObj("tdFuel_Exp");
                var tdFuel_Amt = GetObj("tdFuel_Amt");
                var tdFuel_Inf = GetObj("tdFuel_Inf");
                tdFuel_Exp.innerHTML = " =";
                tdFuel_Amt.innerHTML = "0원";
                tdFuel_Inf.innerHTML = "&nbsp;";
                var ddlCoupon = GetObj("ddlCoupon");
                fn_DisplayCouponAmtLine(ddlCoupon.selectedIndex > 0);
                var ddlADiscount = GetObj("ddlADiscount");
                fn_DisplayADiscountAmtLine(ddlADiscount.selectedIndex > 0);
                //var tdPriority = GetObj( "tdPriority" );
                //tdPriority.innerHTML = "0원";
                fn_PurchaseSum();
            }
        }

        var down_fuel_amt;  //가는편 유류할증료
        var up_fuel_amt;    //오늘편 유류할증료

        function ReceiveFareCalc() {
            if (m_xmlHTTP != null && m_xmlHTTP.readyState == 4) {		//	이 행의 if문은 그대로 사용한다

                var errNode = SelectSingleNode(m_xmlHTTP, "RESULT/EXCEPTION")[0];		//	예외처리

                // 선택한 운임이 유효하지 않을 경우 라디오버튼 체크 해제
                if (errNode != null) { fn_Invalid_FareCalc(errNode.text); return; }
                if (SelectSingleNode(m_xmlHTTP, "NewDataSet/OW")[0] != null
			        || SelectSingleNode(m_xmlHTTP, "NewDataSet/RT")[0] != null) {

                    var Adult = Number(GetObj("hdnAdult").value);
                    var Disable = Number(GetObj("hdnDisable").value);
                    var DisableSub = Number(GetObj("hdnDisableSub").value);
                    var Etc = Number(GetObj("hdnEtc").value);
                    var Child = Number(GetObj("hdnChild").value);
                    var Infant = Number(GetObj("hdnInfant").value);
                    var Tax_DownLine = Number(GetObj("hdnTax_DownLine").value);
                    var Tax_UpLine = Number(GetObj("hdnTax_UpLine").value);
                    //var Priority = Number( GetObj( "hdnPriority" ).value );
                    var isRoundTrip = GetObj("hdnRoundTrip").value != "false";
                    var isDownline = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW").length > 0;
                    var isUpline = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT").length > 0;
                    //	운임
                    var Total_Amt = 0;
                    var tdTotal_Exp = GetObj("tdTotal_Exp");
                    var tdTotal_Amt = GetObj("tdTotal_Amt");
                    var tdTotal_Inf = GetObj("tdTotal_Inf");
                    tdTotal_Exp.innerHTML = "";
                    tdTotal_Amt.innerHTML = "";
                    tdTotal_Inf.innerHTML = "";

                    var ddlCoupon = GetObj("ddlCoupon");
                    var coupon = ddlCoupon.value.split("|");
                    var isCouponUse = ddlCoupon.selectedIndex > 0;
                    var ddlADiscount = GetObj("ddlADiscount");
                    var isADiscountUse = ddlADiscount.selectedIndex > 0;

                    if (GetObj("ctl00_ContentPlaceHolder1_hidPurchaseBtnClick").value != "Y") {
                        if (GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked == true) {
                            fn_OpenInformation("", "선택한 항공편이 변경되어 수수료 적용 선택 해제됩니다. 다시 선택하여 주십시오.");
                            GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
                            GetObj("tdPoint").innerHTML = "";
                            GetObj("tbPoint").style["display"] = "none";
                        }
                    }

                    if (isDownline) {
                        var adult_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0;
                        var child_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/CHILD_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/CHILD_AMT")) : 0;
                        var disable_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/HAND_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/HAND_AMT")) : 0;
                        //				var old_amt		= Number(m_xmlHTTP.responseXML.selectNodes("NewDataSet/OW/OLD_AMT")[0].text);
                        //				var student_amt	= Number(m_xmlHTTP.responseXML.selectNodes("NewDataSet/OW/STUDENT_AMT")[0].text);
                        Total_Amt = (adult_amt * (Adult + DisableSub + Etc)) + (child_amt * Child) + (disable_amt * Disable);
                        GetObj("hdnAdultFare").value = adult_amt;
                        GetObj("hdnChildFare").value = child_amt;

                        if (GetObj("hdnGroupYN").value != "Y" && last_focus_fare.name.indexOf("fltlstDownLine") > -1 && GetObj("ctl00_ContentPlaceHolder1_hidPurchaseBtnClick").value != "Y") {
                            if (GetObj("ctl00_ContentPlaceHolder1_hidOnlyChild").value == "Y") {
                                if (checkedFare != child_amt) {
                                    alert("선택한 운임이 변경되었습니다. 운임이 다시 조회 됩니다.");
                                    fn_GetChildFare("ctl00_ContentPlaceHolder1_fltlstDownLine", 0);
                                }
                            }
                            else {
                                if (checkedFare != adult_amt) {
                                    alert("선택한 운임이 변경되었습니다. 운임이 다시 조회 됩니다.");
                                    fn_GetNormalFare("ctl00_ContentPlaceHolder1_fltlstDownLine", 0);
                                }
                            }
                        }
                    }
                    if (isUpline) {
                        var up_adult_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT")) : 0;
                        var up_child_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/CHILD_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/CHILD_AMT")) : 0;
                        var up_disable_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/HAND_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/HAND_AMT")) : 0;
                        //				var up_old_amt		= Number(m_xmlHTTP.responseXML.selectNodes("NewDataSet/RT/OLD_AMT")[0].text);
                        //				var up_student_amt	= Number(m_xmlHTTP.responseXML.selectNodes("NewDataSet/RT/STUDENT_AMT")[0].text);
                        //	경로 할인 및 학생 할인 등 차후에 추가할 예정(위에 변수는 받아놓았지만 아래 계산식에는 포함하지 않음)
                        if (isDownline) {
                            tdTotal_Exp.innerHTML += fn_InsertComma(Total_Amt) + "원";
                            tdTotal_Exp.innerHTML += " + " + fn_InsertComma((up_adult_amt * (Adult + DisableSub + Etc)) + (up_child_amt * Child) + (up_disable_amt * Disable)) + "원";
                        }
                        Total_Amt += (up_adult_amt * (Adult + DisableSub + Etc)) + (up_child_amt * Child) + (up_disable_amt * Disable);
                        GetObj("hdnUpAdultFare").value = up_adult_amt;
                        GetObj("hdnUpChildFare").value = up_child_amt;

                        if (GetObj("hdnGroupYN").value != "Y" && last_focus_fare.name.indexOf("fltlstUpLine") > -1 && GetObj("ctl00_ContentPlaceHolder1_hidPurchaseBtnClick").value != "Y") {
                            if (GetObj("ctl00_ContentPlaceHolder1_hidOnlyChild").value == "Y") {
                                if (checkedFare != up_child_amt) {
                                    alert("선택한 운임이 변경되었습니다. 운임이 다시 조회 됩니다.");
                                    fn_GetChildFare("ctl00_ContentPlaceHolder1_fltlstUpLine", 0);
                                }
                            }
                            else {
                                if (checkedFare != up_adult_amt) {
                                    alert("선택한 운임이 변경되었습니다. 운임이 다시 조회 됩니다.");
                                    fn_GetNormalFare("ctl00_ContentPlaceHolder1_fltlstUpLine", 0);
                                }
                            }
                        }
                    }
                    tdTotal_Exp.innerHTML += " =";
                    tdTotal_Amt.innerHTML = fn_InsertComma(Total_Amt) + "원";
                    tdTotal_Inf.innerHTML += "(";
                    if ((Adult + DisableSub + Etc) > 0) tdTotal_Inf.innerHTML += "성인 " + (Adult + DisableSub + Etc).toString() + "인";
                    if (Child > 0) {
                        if (tdTotal_Inf.innerHTML.length > 1) tdTotal_Inf.innerHTML += ", ";
                        tdTotal_Inf.innerHTML += "소아 " + Child.toString() + "인";
                    }
                    if (Disable > 0) {
                        if (tdTotal_Inf.innerHTML.length > 1) tdTotal_Inf.innerHTML += ", ";
                        tdTotal_Inf.innerHTML += "장애인 " + Disable.toString() + "인";
                    }
                    tdTotal_Inf.innerHTML += ")";

                    //	공항세
                    var total_tax = 0;
                    var tdTax_Exp = GetObj("tdTax_Exp");
                    var tdTax_Amt = GetObj("tdTax_Amt");
                    var tdTax_Inf = GetObj("tdTax_Inf");
                    tdTax_Exp.innerHTML = "";
                    tdTax_Amt.innerHTML = "";
                    tdTax_Inf.innerHTML = "";
                    if (isDownline) {

                        var adt_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/ADT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/ADT")) : 0;
                        var chd_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/CHD").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/CHD")) : 0;
                        var dbl_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/DBL").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/DBL")) : 0;
                        var dsp_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/DSP").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/DSP")) : 0;
                        var etc_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/ETC").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/ETC")) : 0;
                        total_tax = (adt_tax * Adult) + (chd_tax * Child) + (dbl_tax * Disable) + (dsp_tax * DisableSub) + (etc_tax * Etc);

                    }
                    if (isUpline) {
                        var tax_row_idx = (!isDownline && isUpline) ? 0 : 1;
                        var up_adt_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/ADT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/ADT")) : 0;
                        var up_chd_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/CHD").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/CHD")) : 0;
                        var up_dbl_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/DBL").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/DBL")) : 0;
                        var up_dsp_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/DSP").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/DSP")) : 0;
                        var up_etc_tax = SelectSingleNode(m_xmlHTTP, "NewDataSet/TAX/ETC").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/TAX/ETC")) : 0;
                        //	경로 할인 및 학생 할인 등 차후에 추가할 예정(위에 변수는 받아놓았지만 아래 계산식에는 포함하지 않음)
                        if (isDownline) {
                            tdTax_Exp.innerHTML += fn_InsertComma(total_tax) + "원";
                            tdTax_Exp.innerHTML += " + " + fn_InsertComma((up_adt_tax * Adult) + (up_chd_tax * Child) + (up_dbl_tax * Disable) + (up_dsp_tax * DisableSub) + (up_etc_tax * Etc)) + "원";
                        }
                        total_tax += (up_adt_tax * Adult) + (up_chd_tax * Child) + (up_dbl_tax * Disable) + (up_dsp_tax * DisableSub) + (up_etc_tax * Etc);
                    }
                    tdTax_Exp.innerHTML += " =";
                    tdTax_Amt.innerHTML = fn_InsertComma(total_tax) + "원";
                    tdTax_Inf.innerHTML += "(";
                    if (Adult > 0) tdTax_Inf.innerHTML += "성인 " + Adult.toString() + "인";
                    if (Child > 0) {
                        if (tdTax_Inf.innerHTML.length > 1) tdTax_Inf.innerHTML += ", ";
                        tdTax_Inf.innerHTML += "소아 " + Child.toString() + "인";
                    }
                    if (Disable > 0) {
                        if (tdTax_Inf.innerHTML.length > 1) tdTax_Inf.innerHTML += ", ";
                        tdTax_Inf.innerHTML += "장애인 " + Disable.toString() + "인";
                    }
                    if (DisableSub > 0) {
                        if (tdTax_Inf.innerHTML.length > 1) tdTax_Inf.innerHTML += ", ";
                        tdTax_Inf.innerHTML += "장애인동반 " + DisableSub.toString() + "인";
                    }
                    if (Etc > 0) {
                        if (tdTax_Inf.innerHTML.length > 1) tdTax_Inf.innerHTML += ", ";
                        tdTax_Inf.innerHTML += "기타할인대상 " + Etc.toString() + "인";
                    }
                    tdTax_Inf.innerHTML += ")";

                    //유류할증료
                    var total_fuel = 0;
                    var tdFuel_Exp = GetObj("tdFuel_Exp");
                    var tdFuel_Amt = GetObj("tdFuel_Amt");
                    var tdFuel_Inf = GetObj("tdFuel_Inf");
                    tdFuel_Exp.innerHTML = "";
                    tdFuel_Amt.innerHTML = "";
                    tdFuel_Inf.innerHTML = "";

                    if (isDownline) {
                        var fuel_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/FUEL_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/FUEL_AMT")) : 0;
                        down_fuel_amt = fuel_amt; //가는편 유류할증료를 static 변수에 저장				
                        total_fuel = (fuel_amt * (Adult + DisableSub + Etc + Child + Disable));
                    }
                    if (isUpline) {
                        var fuel_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/FUEL_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/FUEL_AMT")) : 0;
                        up_fuel_amt = fuel_amt; //오는편 유류할증료를 static 변수에 저장	

                        if (isDownline) {
                            tdFuel_Exp.innerHTML += fn_InsertComma(total_fuel) + "원";
                            var up_total_fuel = fuel_amt * (Adult + DisableSub + Etc + Child + Disable);
                            tdFuel_Exp.innerHTML += " + " + fn_InsertComma(up_total_fuel) + "원";
                        }
                        total_fuel += up_total_fuel;
                    }

                    tdFuel_Exp.innerHTML += " =";
                    tdFuel_Amt.innerHTML = fn_InsertComma(total_fuel) + "원";
                    tdFuel_Inf.innerHTML += "(";
                    if ((Adult + DisableSub + Etc) > 0) tdFuel_Inf.innerHTML += "성인 " + (Adult + DisableSub + Etc).toString() + "인";
                    if (Child > 0) {
                        if (tdFuel_Inf.innerHTML.length > 1) tdFuel_Inf.innerHTML += ", ";
                        tdFuel_Inf.innerHTML += "소아 " + Child.toString() + "인";
                    }
                    if (Disable > 0) {
                        if (tdFuel_Inf.innerHTML.length > 1) tdFuel_Inf.innerHTML += ", ";
                        tdFuel_Inf.innerHTML += "장애인 " + Disable.toString() + "인";
                    }
                    tdFuel_Inf.innerHTML += ")";

                    //	쿠폰
                    var coupon_pax_gubun = "";
                    //쿠폰 선택된 탑승객의 신분 가져오기
                    var tblPassengerList = GetObj("tblPassengerList");
                    if (tblPassengerList != false) {
                        for (var i = 0; i < tblPassengerList.rows.length; i++) {
                            var row = tblPassengerList.rows[i];
                            if (row.cells[0].children[0].tagName == "IMG") continue;
                            if (row.cells[2].children[0].checked) {
                                coupon_pax_gubun = row.cells[0].children[0].value;
                                break;
                            }
                        }
                    }
                    var coupon_display = (isCouponUse && !IsEmpty(coupon_pax_gubun));

                    //쿠폰
                    fn_DisplayCouponAmtLine(coupon_display);
                    //이벤트할인
                    fn_DisplayADiscountAmtLine(isADiscountUse);

                    //	최종 지불금액
                    fn_PurchaseSum();
                }
            }
        }

        function fn_Invalid_FareCalc(err_text) {
            if (last_focus_fare != null) {
                last_focus_fare.checked = false;
                var fltlst_id = fn_Right(last_focus_fare.name, last_focus_fare.name.length - 3);
                GetObj(fltlst_id + "_hdnFLT_NUM").value = "";
                GetObj(fltlst_id + "_hdnBookingClass").value = "";
                fn_SetSummaryText();
            }
        }

        //	최종 지불금액
        function fn_PurchaseSum() {
            var Total_Amt = fn_GetValue("tdTotal_Amt");
            var Tax_Amt = fn_GetValue("tdTax_Amt");
            var Fuel_Amt = fn_GetValue("tdFuel_Amt");
            var Coupon_Amt = fn_GetValue("tdCoupon_Amt");
            var ADiscount_Amt = fn_GetValue("tdADiscount_Amt");
            //var Priority = fn_GetValue( "tdPriority" );
            var tdPurchase = GetObj("tdPurchase");

            //var tatal_sum = Total_Amt + Tax_Amt + Fuel_Amt + Coupon_Amt + Priority + ADiscount_Amt;
            var tatal_sum = Total_Amt + Tax_Amt + Fuel_Amt + Coupon_Amt + ADiscount_Amt;
            tdPurchase.innerHTML = fn_InsertComma(tatal_sum) + "원";

            GetObj("price").value = tatal_sum;
            GetObj("EP_product_type").value = tatal_sum;

            var tdPoint = fn_GetValue("tdPoint");
            GetObj("tdTotal").innerHTML = fn_InsertComma(tatal_sum + tdPoint) + "원";
        }

        function fn_GetValue(td_id) {
            var td = GetObj(td_id);
            var td_value = 0;
            if (td.innerHTML && td.innerHTML != "" && td.innerHTML != "&nbsp;") {
                var td_text = fn_DeleteComma(fn_Trim(td.innerHTML).replace("원", ""));
                if (!isNaN(td_text))
                    td_value = Number(td_text);
            }
            return td_value;
        }

        function fn_GetSelectedValue_Radio(radio_name) {
            var radios = document.getElementsByName(radio_name);
            if (radios == null || radios.length <= 0)
                radios = document.getElementsByName(vG_ContentPrefixName + radio_name);
            for (var i = 0; i < radios.length; i++) {
                if (!radios[i].disabled && radios[i].checked) {
                    return radios[i].value;
                }
            }
            return "";
        }

        function fn_RadioDisable_Toggle(radio_name, enable) {
            var radios = document.getElementsByName(radio_name);
            if (radios == null || radios.length <= 0)
                radios = document.getElementsByName(vG_ContentPrefixName + radio_name);
            for (var i = 0; i < radios.length; i++) {
                if (enable != null) {
                    if (!enable && radios[i].value == "N") {
                        radios[i].checked = true;
                    }
                    radios[i].disabled = !enable;
                }
                else {
                    radios[i].disabled = !radios[i].disabled;
                }
            }
        }

        function fn_Validation() {

            var tdValidationInfo = GetObj("ctl00_ContentPlaceHolder1_tdValidationInfo");
            tdValidationInfo.innerHTML = "&nbsp;";
            var focus_control = null;
            var isRoundTrip = GetObj("hdnRoundTrip").value != "false";
            var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
            var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
            var message_text = "";

            var isValid = true;


            // 2015-01-05 정신철 기업할인 유효성 검사 추가
            var discountInfo = $("#ctl00_ContentPlaceHolder1_hidADiscountInfoOW").val();
            if ($.trim(discountInfo)) {
                var arrDiscountInfo = discountInfo.split('$');
                var aDisOWValueIndex = 0;
                for (var i = 0; i < arrDiscountInfo.length - 1; i++) {
                    if ($("#ctl00_ContentPlaceHolder1_ddlADiscount").val() == arrDiscountInfo[i].split(";")[0])  // 2015-01-05 정신철 기업할인 처리를 위해 문자열 구분 처리 추가
                    {
                        aDisOWValueIndex = i;
                        break;
                    }
                }
                var rdoADiscountIsUse01 = GetObj("ctl00_ContentPlaceHolder1_rdoADiscountIsUse01");
                var arrDiscountValue = arrDiscountInfo[aDisOWValueIndex].split(';');
                if (arrDiscountValue[16] == "T" && rdoADiscountIsUse01.checked) {
                    if (!GetObj("ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").checked) {
                        message_text += "\r\n기업 우대 할인 이용 규정에 동의하셔야 구매가 가능합니다.";
                        focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree");
                        isValid = false;
                    }
                }
            }
            //	전자결제서비스 이용약관에 동의
            if (GetObj("ctl00_ContentPlaceHolder1_rdoCard").checked) {
                if (GetObj("chkPayAgree").checked != true) {
                    message_text += "\r\n전자결제서비스 이용약관에 동의하지 않으셨습니다.";
                    focus_control = focus_control != null ? focus_control : GetObj("chkPayAgree");
                    isValid = false;
                }
            }

            //	운임규정에 동의
            if (GetObj("chkAgree").checked != true) {
                message_text += "\r\n운임규정에 동의하지 않으셨습니다.";
                focus_control = focus_control != null ? focus_control : GetObj("chkAgree");
                isValid = false;
            }

            //	운임 선택 확인
            var isFareDriven = GetObj("hdnIsFareDriven").value == "Y";
            var downline_class, upline_class;
            if (isFareDriven) {
                downline_class = GetObj(downline_id + "_hdnBookingClass").value;
                upline_class = GetObj(upline_id + "_hdnBookingClass").value;
            }
            else {
                downline_class = fn_GetSelectedValue_Radio("rdo" + downline_id);
                upline_class = fn_GetSelectedValue_Radio("rdo" + upline_id);
            }
            if (IsEmpty(downline_class) && IsEmpty(upline_class)) {
                message_text += "\r\n운임을 선택하지 않으셨습니다. 만일 모두 매진이라면 이전날, 다음날을 조회하실 수도 있습니다.";
                isValid = false;
            }

            //	가는날이 오는날 보다 과거인지 확인
            var down_date = GetObj(downline_id + "_hdnDate").value;
            var up_date = GetObj(upline_id + "_hdnDate").value;

            var down_visible = GetObj(downline_id + "_hdnVisible").value != "false";
            var up_visible = GetObj(upline_id + "_hdnVisible").value != "false";
            var down_dept_arrt = GetObj(downline_id + "_hdnDEPT_ARRT").value;
            var up_dept_arrt = GetObj(upline_id + "_hdnDEPT_ARRT").value;
            var arr_down_dept_arrt = down_dept_arrt.split("-");
            var arr_up_dept_arrt = up_dept_arrt.split("-");
            if ((down_visible && up_visible) && down_date > up_date) {
                message_text += "\r\n오는날이 가는날보다 더 빠릅니다.";
                isValid = false;
            }
                //	같은 날일 때 오는 편의 출발시간이 가는 편의 도착시간보다 빠른지 확인.
            else if ((down_visible && up_visible) && (!IsEmpty(down_dept_arrt) && !IsEmpty(up_dept_arrt)) && (arr_down_dept_arrt != null && arr_down_dept_arrt.length > 1) && (arr_up_dept_arrt != null && arr_up_dept_arrt.length > 1)) {
                var down_arr_dt = fn_GetFlightDateTime(down_date, arr_down_dept_arrt[1]);
                var up_dep_dt = fn_GetFlightDateTime(up_date, arr_up_dept_arrt[0]);
                var add_hour = up_dep_dt.getTime() - (60 * 60000);	//	1시간을 뺀다.
                var trans_added_dt = new Date(2017, (4 -1), 21, 16, 59, 3);
                trans_added_dt.setTime(add_hour);
                if (isRoundTrip && down_arr_dt > up_dep_dt) {
                    message_text += "\r\n오는편의 출발시간이 가는편의 도착시간보다 더 빠릅니다.";
                    isValid = false;
                }
                else if (isRoundTrip && down_arr_dt <= up_dep_dt && down_arr_dt > trans_added_dt) {
                    message_text += "\r\n가는편 도착 후 오는편을 타기 위한 시간이 너무 짧습니다.";
                    isValid = false;
                }
            }
        var adult = 0, child = 0, infant = 0, disable = 0, disableSub = 0, etc = 0;
        var tblPassengerList = GetObj("tblPassengerList");
        var ddlCoupon = GetObj("ddlCoupon");
        var isCouponUsed = false;   // 쿠폰 사용여부 저장하기 위한 변수

            //쿠폰이 EMBARGO 기간에 포함되었는지
        if (fn_Valid_Embargo()) {
            message_text += "\r\n쿠폰 성수기 기간으로 쿠폰 이용이 불가능입니다. (" + embargo_range + ")\r\n쿠폰을 적용하지 않으시려면 쿠폰을 \"선택\"으로 변경하여 주세요.";
            isValid = false;
        }

        for (var i = 0; i < tblPassengerList.rows.length; i++) {
            if (tblPassengerList.rows[i].cells[0].children[0].tagName == "IMG") continue;
            var gubun_value = tblPassengerList.rows[i].cells[0].children[0].value;
            var gubun = tblPassengerList.rows[i].cells[0].innerHTML.Trim();
            var pax_name = tblPassengerList.rows[i].cells[4].children[0].value.toUpperCase() + tblPassengerList.rows[i].cells[5].children[0].value.toUpperCase();
            var pax_family_name = tblPassengerList.rows[i].cells[4].children[0].value.toUpperCase();
            var pax_given_name = tblPassengerList.rows[i].cells[5].children[0].value.toUpperCase();
            var pax_dob = tblPassengerList.rows[i].cells[6].children[0].value;
            var hdnDOB_Ignore = tblPassengerList.rows[i].cells[6].children[4];

            switch (gubun_value) {
                case "Adult": adult++; break;
                case "Disable": disable++; break;
                case "DisableSub": disableSub++; break;
                case "Etc": etc++; break;
                case "Child": child++; break;
                case "Infant": infant++; break;
                default: break;
            }
            var message_name = "";
            //	쿠폰을 적용했는지 변수에 저장
            if (ddlCoupon.selectedIndex > 0) {
                if (!isCouponUsed && tblPassengerList.rows[i].cells[2].children[0].checked) {
                    isCouponUsed = true;
                }
            }

            //	탑승객 정보 성 입력 확인
            if (IsEmpty(pax_family_name) || pax_family_name == "-성-") {
                message_name = "\r\n" + gubun + " 탑승객의 이름을 입력해주세요.";
                focus_control = focus_control != null ? focus_control : tblPassengerList.rows[i].cells[4].children[0];
                isValid = false;
            }

            //	탑승객 정보 이름 입력 확인
            if (IsEmpty(pax_given_name) || pax_given_name == "-이름-") {
                message_name = "\r\n" + gubun + " 탑승객의 이름을 입력해주세요.";
                focus_control = focus_control != null ? focus_control : tblPassengerList.rows[i].cells[5].children[0];
                isValid = false;
            }
            if (!IsEmpty(message_name))
                message_text += message_name;

            if (!IsEmpty(pax_name)) {
                //	탑승객 이름에 한글과 영문이 혼용되었는지 확인
                if (!fn_Valid_EngKor_Name(pax_name)) {
                    message_text += "\r\n" + gubun + " 탑승객의 이름에 한글과 영문이 혼용되었습니다. 영문 또는 한글만으로 입력해주세요.";
                    if (!fn_Valid_EngKor_Name(pax_family_name)) {
                        focus_control = focus_control != null ? focus_control : tblPassengerList.rows[i].cells[4].children[0];
                    }
                    else {
                        focus_control = focus_control != null ? focus_control : tblPassengerList.rows[i].cells[5].children[0];
                    }
                    isValid = false;
                }
            }

            //	소아, 유아의 생일 입력 확인
            if ((gubun_value == "Child" || gubun_value == "Infant") && (pax_dob == null || pax_dob == "")) {
                message_text += "\r\n" + gubun + " 탑승객인 " + ((gubun_value == "Child") ? "소아" : "유아") + "의 생년월일을 입력해주세요.";
                focus_control = focus_control != null ? focus_control : tblPassengerList.rows[i].cells[6].children[2];
                isValid = false;
            }
            //	입력 날짜가 유효한 날짜인지 확인
            if (!IsValidDate(pax_dob) || !IsValidPast(pax_dob, new Date(2017, (4 -1), 21, 16, 59, 3))) {
                message_text += "\r\n" + gubun + " 탑승객인 " + ((gubun_value == "Child") ? "소아" : "유아") + "의 생년월일을 유효한 날짜로 입력해주세요.";
                focus_control = focus_control != null ? focus_control : tblPassengerList.rows[i].cells[6].children[2];
                isValid = false;
            }
            //	유아, 소아 생년월일 확인 (가는날 기준 소아는 만 13세 미만, 유아는 24개월 미만)
            if (gubun_value == "Child" || gubun_value == "Infant") {
                var max_age = (gubun_value == "Child") ? 13 : 2;
                if (!isValidMaxAge(pax_dob, max_age, GetObj(downline_id + "_hdnDate").value)) {
                    if (fn_OpenConfirm("", gubun + " 탑승객은 출발일 기준으로 만 " + (max_age).toString() + "세 이상으로 " + ((gubun_value == "Child") ? "성인" : "소아") + "에 해당됩니다."
                                            + "\r\n[확인]을 누르시면 " + ((gubun_value == "Child") ? "성인" : "소아") + " 요금으로 재계산됩니다."
                                            + "\r\n만일 생년월일을 잘못 입력하셔서 수정하고자 하신다면 [취소]를 눌러주세요.")) {
                        fn_PaxGubun_Change(tblPassengerList.rows[i].cells[0].children[0], gubun_value, ((gubun_value == "Child") ? "Adult" : "Child"));
                    }
                    else {
                        tblPassengerList.rows[i].cells[6].children[1].focus();
                        if (tblPassengerList.rows[i].cells[6].children[1].select)
                            tblPassengerList.rows[i].cells[6].children[1].select();
                        return false;
                    }
                }
                else if (gubun_value == "Child" && hdnDOB_Ignore.value != "ignore" && !IsEmpty(pax_dob) && isValidMaxAge(pax_dob, 2, GetObj(downline_id + "_hdnDate").value)) {
                    if (fn_OpenConfirm("", gubun + " 탑승객은 출발일 기준으로 만 2세 미만으로 유아에 해당됩니다."
                                            + "\r\n[확인]을 누르시면 소아 요금이 적용됩니다."
                                            + "\r\n유아 운임을 적용하려면 [취소]를 눌러 주세요.")) {
                        //생일은 유아이지만 소아요금이 적용됩니다. 플래그를 생일 무시로 변경해줍니다.
                        hdnDOB_Ignore.value = "ignore";
                        fn_PaxGubun_Change(tblPassengerList.rows[i].cells[0].children[0], gubun_value, "Child");
                    }
                    else {
                        //유아로 신분을 변경합니다. 플래그를 변경됨으로 변경해 줍니다.
                        fn_PaxGubun_Change(tblPassengerList.rows[i].cells[0].children[0], gubun_value, "Infant");
                        hdnDOB_Ignore.value = "changed";
                    }
                }
            }

        }
            //	최대 인원 확인
        if ((adult + child + disable + disableSub + etc) > 9) {
            message_text += "\r\n유아를 제외한 탑승객 인원이 9명 이하이어야 합니다.";
            isValid = false;
        }
            //	유아 보호자 인원 확인
        if ((adult + disable + disableSub + etc) < infant) {
            message_text += "\r\n유아인원이 보호자 인원보다 많습니다.";
            isValid = false;
        }
            //	소아 동반 성인 확인
        if (child > 0 && (adult + disable + disableSub + etc) <= 0) {
            if (GetObj("ctl00_ContentPlaceHolder1_hdnOnlyChild").value != "Y") {
                message_text += "\r\n소아발권은 탑승자 정보 입력 및 확인이 필요합니다.";
                isValid = false;
            }
        }
            //	쿠폰 선택 확인
        if (ddlCoupon.selectedIndex > 0 && !isCouponUsed) {
            message_text += "\r\n쿠폰을 적용할 탑승객을 선택하세요. 쿠폰을 적용하지 않으시려면 쿠폰을 \"선택\"으로 변경하여 주세요.";
            isValid = false;
        }
        if (!IsEmpty(GetObj("ctl00_ContentPlaceHolder1_txtMobile").value) && GetObj("ctl00_ContentPlaceHolder1_txtMobile").value.length < 10) {
            message_text += "\r\n휴대폰 번호가 유효하지 않습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtMobile");
            isValid = false;
        }
        else if (!IsEmpty(GetObj("ctl00_ContentPlaceHolder1_txtMobile").value) && !checkMobile(GetObj("ctl00_ContentPlaceHolder1_txtMobile").value)) {
            message_text += "\r\n휴대폰 번호가 유효하지 않습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtMobile");
            isValid = false;
        }

            // 카드 선택 확인 추가 2016-07-21 정신철 카드 선택 유효성 검사
    if (GetObj("ctl00_ContentPlaceHolder1_rdoCard").checked) {
                if (!$('#ctl00_ContentPlaceHolder1_ddl_card_cd').val()) {
            alert("신용카드를 선택하세요.!!");
            $('#ctl00_ContentPlaceHolder1_ddl_card_cd').focus();
            return;
        }
    }

            //	이메일 확인
    var email = GetObj("ctl00_ContentPlaceHolder1_txtEmail").value;

            if (!IsEmpty(email) && !email.IsEmail()) {
                message_text += "\r\n이메일 주소를 (xxx@sample.com)와 같은 형식으로 입력하세요.";
                focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtEmail");
                isValid = false;
            }

            if (GetObj("ctl00_ContentPlaceHolder1_rdoPrivateCard").checked) {
                var cardNo01 = GetObj("txtCardNo01");
                var cardNo02 = GetObj("txtCardNo02");
                var cardNo03 = GetObj("txtCardNo03");
                var cardNo04 = GetObj("txtCardNo04");
                var expDateYear = GetObj("ddlExpDateYear");
                var expDateMonth = GetObj("ddlExpDateMonth");
                var cardPasswd = GetObj("txtCardPasswd");
                var authNo = GetObj("txtAuthNo");

                if (cardNo01.value.Trim() == "" || cardNo02.value.Trim() == "" || cardNo03.value.Trim() == "" || cardNo04.value.Trim() == "") {
                    message_text += "\r\n카드번호를 입력하세요.";
                    isValid = false;
                }
                if (expDateYear.value.Trim() == "") {
                    message_text += "\r\n유효기간 년을 선택하세요.";
                    isValid = false;
                }
                if (expDateMonth.value.Trim() == "") {
                    message_text += "\r\n유효기간 월을 선택하세요.";
                    isValid = false;
                }
                if (authNo.value.Trim() == "") {
                    message_text += "\r\n인증번호를 입력하세요.";
                    isValid = false;
                }
            }

            //	메시지 띄우기
            if (!isValid) {
                if (message_text != "") {
                    tdValidationInfo.innerHTML = fn_GetHTML_MessageBox(message_text);	//	message_text.Trim().ReplaceAll("\r\n", "<br />");
                }
                if (focus_control != null) {
                    focus_control.focus();
                    if (focus_control.select)
                        focus_control.select();
                }
                return false;
            }
            //	선택사항 확인 confirm 로직
            //	왕복인데 편도만 선택했을 경우 계속 조회 권유
            if (isValid && isRoundTrip && (downline_class == "" || upline_class == "")) {
                if (fn_OpenConfirm("", "왕복 여정 중에 일부 여정의 운임을 선택하지 않으셨습니다.\r\n만일 모두 매진이라면 이전날, 다음날을 조회하실 수도 있습니다.\r\n"
								        + "편도만 선택하신 채로 구매를 계속 진행하고자 한다면 [취소]를,\r\n이전날, 다음날을 더 조회하시려면 [확인]을 눌러주세요")) {
                    isValid = false;
                }
                else {
                    isValid = true;
                    isRoundTrip = false;
                    GetObj("hdnRoundTrip").value = "false";
                }
            }

            if (!isIE() && GetObj("ctl00_ContentPlaceHolder1_rdoBank").checked) {
                alert("익스플로러에서만 실시간계좌이체 결제가 가능합니다.(" + BrowserDetect.browser + ")");
                return false;
            }

            var msg = "";
            if (downline_class == "E" || upline_class == "E") {
                msg = "〈 환불 위약금 안내 〉\n\n";
                msg += "출발 60일전 ~ 31일전 : 편도 1인당 1천원 \n";
                msg += "출발 30일전 ~ 출발 8일전 : 편도 1인당 2천원\n";
                msg += "출발 7일전 ~ 출발 2일전 : 편도 1인당 3천원\n";
                msg += "출발 1일전 ~ 출발시간 : 편도 1인당 8천원\n";
                msg += "출발 예정시간 이후 : 편도 1인당 1만 2천원\n";
                msg += "(최초 예매 당일에는 위약금이 면제 됩니다.)\n\n\n";
                msg += "예매하시겠습니까?";
            }
            else {
                msg = "〈 환불 위약금 안내 〉\n\n";
                msg += "출발 60일전 ~ 31일전 : 편도 1인당 1천원 \n";
                msg += "출발 30일전 ~ 출발 8일전 : 편도 1인당 2천원\n";
                msg += "출발 7일전 ~ 출발 2일전 : 편도 1인당 3천원\n";
                msg += "출발 1일전 ~ 출발시간 : 편도 1인당 8천원\n";
                msg += "출발 예정시간 이후 : 편도 1인당 1만 2천원\n";
                msg += "(최초 예매 당일에는 위약금이 면제 됩니다.)\n\n\n";
                msg += "예매하시겠습니까?";
            }

            var result = isValid && fn_OpenConfirm("", msg);
            if (result) {
                ProgressBar("purchase");
                RequestReservation() // 기존 fn_RequestReservation();
                return false;
            }
            return result;
        }

        function fn_GetHTML_MessageBox(message_text) {
            var return_html = "\r\n<table width=\"670\" style=\"margin-left:20px;margin-right:20px;\" border=\"0\" cellpadding=\"10\" cellspacing=\"1\" bordercolor=\"#FFFFFF\" bgcolor=\"#ffae7f\">";
            return_html += "\r\n\t<tr>\r\n\t\t<td bgcolor=\"#FFFFFF\">\r\n\t\t\t<ul style=\"margin:0px;list-style-type:disc;\">";
            var messages = message_text.Trim().split("\r\n");
            for (var i = 0; i < messages.length; i++) {
                return_html += "\r\n\t\t\t\t<li class=\"Cpinkday\" style=\"text-align:left;list-style-type:disc;\">";
                return_html += messages[i];
                return_html += "</li>";
            }
            return_html += "\r\n\t\t\t</ul>\r\n\t\t</td>\r\n\t</tr>\r\n</table>";
            return return_html;
        }

        function fn_Validation_Login() {
            var tdValidationInfo = GetObj("ctl00_ContentPlaceHolder1_tdValidationInfo");
            tdValidationInfo.innerHTML = "&nbsp;";
            var focus_control = null;
            var isRoundTrip = GetObj("hdnRoundTrip").value != "false";
            var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
            var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
            var message_text = "";
            var isValid = true;
            //	가는날이 오는날 보다 과거인지 확인
            var down_date = GetObj(downline_id + "_hdnDate").value;
            var up_date = GetObj(upline_id + "_hdnDate").value;

            var down_visible = GetObj(downline_id + "_hdnVisible").value != "false";
            var up_visible = GetObj(upline_id + "_hdnVisible").value != "false";
            var down_dept_arrt = GetObj(downline_id + "_hdnDEPT_ARRT").value;
            var up_dept_arrt = GetObj(upline_id + "_hdnDEPT_ARRT").value;
            var arr_down_dept_arrt = down_dept_arrt.split("-");
            var arr_up_dept_arrt = up_dept_arrt.split("-");
            if ((down_visible && up_visible) && down_date > up_date) {
                message_text += "\r\n오는날이 가는날보다 더 빠릅니다.";
                isValid = false;
            }
                //	같은 날일 때 오는 편의 출발시간이 가는 편의 도착시간보다 빠른지 확인.
            else if ((down_visible && up_visible) && (!IsEmpty(down_dept_arrt) && !IsEmpty(up_dept_arrt)) && (arr_down_dept_arrt != null && arr_down_dept_arrt.length > 1) && (arr_up_dept_arrt != null && arr_up_dept_arrt.length > 1)) {
                var down_arr_dt = fn_GetFlightDateTime(down_date, arr_down_dept_arrt[1]);
                var up_dep_dt = fn_GetFlightDateTime(up_date, arr_up_dept_arrt[0]);
                var add_hour = up_dep_dt.getTime() - (60 * 60000);	//	1시간을 뺀다.
                var trans_added_dt = new Date(2017, (4 -1), 21, 16, 59, 3);
                trans_added_dt.setTime(add_hour);
                if (isRoundTrip && down_arr_dt > up_dep_dt) {
                    message_text += "\r\n오는편의 출발시간이 가는편의 도착시간보다 더 빠릅니다.";
                    isValid = false;
                }
                else if (isRoundTrip && down_arr_dt <= up_dep_dt && down_arr_dt > trans_added_dt) {
                    message_text += "\r\n가는편 도착 후 오는편을 타기 위한 시간이 너무 짧습니다.";
                    isValid = false;
                }
            }
            //	메시지 띄우기
        if (!isValid) {
            if (message_text != "") {
                tdValidationInfo.innerHTML = fn_GetHTML_MessageBox(message_text);	//	message_text.Trim().ReplaceAll("\r\n", "<br />");
            }
            if (focus_control != null) {
                focus_control.focus();
                if (focus_control.select)
                    focus_control.select();
            }
            return false;
        }
        return isValid;
    }

    function fn_ddlDOB_Change(e) {
        var evt = window.event || e;
        var src = GetEventToggle(evt);
        var td = GetParent_by_Tag("TD", src);
        var hdnDOB = td.children[0];
        var ddl_Y = td.children[1];
        var ddl_M = td.children[2];
        var ddl_D = td.children[3];
        var hdnDOB_Ignore = td.children[4];
        var date_text = ddl_Y.value + ddl_M.value + ddl_D.value;
        var date_string = ddl_Y.value + "년 " + ddl_M.value + "월 " + ddl_D.value + "일";
        var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
        var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine"; // 2014-04-22 정신철 추가
        var tr = GetParent_by_Tag("TR", src);
        var gubun_value = tr.cells[0].children[0].value;
        var gubun = tr.cells[0].children[2].value;
        var isRoundTrip = GetObj("hdnRoundTrip").value; // 2014-04-22 정신철 추가 'true':왕복, 'false':편도
        var current_gubun_value = gubun_value; // 2014-04-22 정신철 추가 'true':왕복, 'false':편도
        hdnDOB.value = date_text;
        //	입력 날짜가 유효한 날짜인지 확인
        if (!IsValidDate(date_text) || !IsValidPast(date_text, new Date(2017, (4 -1), 21, 16, 59, 3))) {
            alert(gubun + " 탑승객의 생년월일을 유효한 날짜로 입력해주세요.");
            if (ddl_D != null) {
                ddl_D.focus();
                if (ddl_D.select)
                    ddl_D.select();
            }
            return false;
        }
        //	유아, 소아 생년월일 확인 (가는날 기준 소아는 만 13세 미만, 유아는 24개월 미만)
        if (gubun_value == "Child" || gubun_value == "Infant") {
            var max_age = (gubun_value == "Child") ? 13 : 2;
            if (!isValidMaxAge(date_text, max_age, GetObj(downline_id + "_hdnDate").value)) {
                hdnDOB_Ignore.value = "";
                if (fn_OpenConfirm("", gubun + " 탑승객은 출발일 기준으로 만 " + (max_age).toString() + "세 이상으로 " + ((gubun_value == "Child") ? "성인" : "소아") + "에 해당됩니다."
                                        + "\r\n[확인]을 누르시면 " + ((gubun_value == "Child") ? "성인" : "소아") + " 요금으로 재계산됩니다."
                                        + "\r\n만일 " + gubun + " 탑승객의 생일이 " + date_string + "이 아니라면 [취소]를 눌러 수정해주세요.")) {
                    fn_PaxGubun_Change(tr.cells[0].children[0], gubun_value, ((gubun_value == "Child") ? "Adult" : "Child"));
                    current_gubun_value = (gubun_value == "Child") ? "Adult" : "Child"; // 2014-04-22 정신철 추가
                }
                else {
                    if (src != null) {
                        src.focus();
                        if (src.select)
                            src.select();
                    }
                    return false;
                }
            }
            else if (gubun_value == "Child" && hdnDOB_Ignore.value != "ignore" && !IsEmpty(date_text) && isValidMaxAge(date_text, 2, GetObj(downline_id + "_hdnDate").value)) {
                if (fn_OpenConfirm("", gubun + "  탑승객은 출발일 기준으로 만 2세 미만으로 유아에 해당됩니다."
                                            + "\r\n[확인]을 누르시면 소아 요금이 적용됩니다."
                                            + "\r\n유아 운임을 적용하려면 [취소]를 눌러 주세요.")) {
                    //생일은 유아이지만 소아요금이 적용됩니다. 플래그를 생일 무시로 변경해줍니다.
                    hdnDOB_Ignore.value = "ignore";
                }
                else {
                    //유아로 신분을 변경합니다. 플래그를 변경됨으로 변경해 줍니다.
                    fn_PaxGubun_Change(tr.cells[0].children[0], gubun_value, "Infant");
                    hdnDOB_Ignore.value = "changed";
                    current_gubun_value = "Infant"; // 2014-04-22 정신철 추가
                }
            }

            // 2014-04-22 정신철 왕복일 오는날 기준 상태 확인(성인/소아/유아)
            if (isRoundTrip == 'true' && current_gubun_value != "Adult") {
                var max_age = (current_gubun_value == "Child") ? 13 : 2;
                if (current_gubun_value == "Child") { // 소아 대상자들
                    if (!isValidMaxAge(date_text, max_age, GetObj(upline_id + "_hdnDate").value)) {
                        alert(gubun + " 탑승객은 오는날 기준으로 만 " + (max_age).toString() + "세 이상으로 성인에 해당됩니다."
                                        + "\r\n가는편(소아), 오는편(성인)을 따로 예약해 주세요."
                                        + "\r\n"
                                        + "\r\n* 탑승 당일 공항에서 소아가 아님이 확인될 경우, 환불 후 재구매하셔야 합니다. (재구매 시점의 성인운임 적용)"
                        );
                    }
                }
                else { // 유아 대상자들
                    if (!isValidMaxAge(date_text, max_age, GetObj(upline_id + "_hdnDate").value)) {
                        alert(gubun + " 탑승객은 오는날 기준으로 만 " + (max_age).toString() + "세 이상으로 소아에 해당합니다."
                                        + "\r\n가는편(유아), 오는편(소아)을 따로 예약해 주세요."
                                        + "\r\n"
                                        + "\r\n* 탑승 당일 공항에서 유아가 아님이 확인될 경우, 현장 판매 소아 운임으로 추가 구매 후 탑승이 가능합니다. (여유좌석이 있는 경우에 한함)"
                        );
                    }
                }
            }
        }
        return true;
    }

    function fn_GetFlightDateTime(s_date, s_time) {
        var dt = null;
        try {
            dt = GetDate(s_date);
            var times = s_time.split(":");
            var h = Number(times[0]);
            var m = Number(times[1]);
            dt.setHours(h, m);
        }
        catch (e) { }
        return dt;
    }

    function fn_PaxGubun_Change(hdn_control, invalid_gubun, valid_gubun) {
        var invalid_cnt = Number(GetObj("hdn" + invalid_gubun).value);
        var valid_cnt = Number(GetObj("hdn" + valid_gubun).value);
        GetObj("hdn" + invalid_gubun).value = (invalid_cnt - 1).toString();
        GetObj("hdn" + valid_gubun).value = (valid_cnt + 1).toString();
        hdn_control.value = valid_gubun;
        fn_FillPaxList(true);
        fn_SetSummaryText();

        // 2014-04-23 정신철 구분 변경 시 fn_FillPaxList()에서 날짜 초기화 하지 않고 해당 신분이 변경됐음으로 (유아 ↔ 소아) 년도를 바꿔준다.
        if (valid_gubun == "Child" || valid_gubun == "Infant") {
            var ddlctrl = $(hdn_control).parent().eq(0).parent().children().find('select').eq(1); // 년도 드롭다운 객체
            fn_initDateYear(ddlctrl, valid_gubun == "Child" ? 13 : 2);
        }
    }

    // 2014-04-23 정신철 구분 변경 시 유아 ↔ 소아 변경 시 년도 리스트 초기화
    function fn_initDateYear(ddlObj, yearCnt) {
        var options = $(ddlObj).prop('options');
        var today = new Date(2017, (4 -1), 21, 16, 59, 3);
        var this_year = today.getFullYear();
        var this_month = today.getMonth();
        var this_day = today.getDate();
        var minYear = this_year - yearCnt;
        var selectedYear = $(ddlObj).find("option:selected").val();
        $(ddlObj).children().remove();
        for (var i = this_year; i >= minYear; i--) {
            options[options.length] = new Option(i + "년", i);
        }
        $(ddlObj).val(selectedYear);
    }

    function fn_IsCoupon_Click(e) {
        var src = GetEventToggle(e);
        var src_checked = src.checked;
        var oContainer = GetParent_by_Tag("TABLE", src);

        for (var i = 0 ; i < oContainer.getElementsByTagName("*").length ; i++) {
            oItem = oContainer.getElementsByTagName("*")[i];
            if (oItem.tagName.toUpperCase() == "INPUT" && oItem.getAttribute("type").toUpperCase() == "CHECKBOX") {
                if (fn_Right(oItem.id, 6) == "Coupon") {
                    if (oItem.checked) {
                        oItem.checked = false;
                    }
                }
            }
        }
        src.checked = src_checked;
        fn_DisplayCouponAmtLine(src_checked);
    }

    function fn_DisplayCouponAmtLine(checked) {
        var tdCoupon_Amt = GetObj("tdCoupon_Amt");
        var trCoupon_Line1 = GetObj("trCoupon_Line1");
        var trCoupon_Line2 = GetObj("trCoupon_Line2");
        var ddlCoupon = GetObj("ddlCoupon");
        var coupon = ddlCoupon.value.split("|");

        if (checked) {

            var pax_gubun = "";
            var fare_amt = -1;
            //쿠폰 선택된 탑승객의 신분 가져오기
            var tblPassengerList = GetObj("tblPassengerList");
            for (var i = 0; i < tblPassengerList.rows.length; i++) {
                var row = tblPassengerList.rows[i];
                if (row.cells[0].children[0].tagName == "IMG") continue;
                if (row.cells[2].children[0].checked) {
                    pax_gubun = row.cells[0].children[0].value;
                    break;
                }
            }
            //신분에 해당하는 요금 가져오기
            if (m_xmlHTTP != null && m_xmlHTTP.readyState == 4) {		//	이 행의 if문은 그대로 사용한다
                switch (pax_gubun) {
                    case "Adult": fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0; break;
                    case "Child": fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/CHILD_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/CHILD_AMT")) : 0; break;
                    case "Infant": fare_amt = 0; break;
                    case "Disable": fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/HAND_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/HAND_AMT")) : 0; break;
                    case "DisableSub": fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0; break;
                    case "Etc": fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0; break;
                    default: fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0; break;
                }
            }

            var coupon_amt = coupon[1];
            var coupon_dis_cla = coupon[10];

            if (coupon_dis_cla != "P")
                coupon_dis_cla = "A";

            if (coupon_dis_cla == "A") {
                if (fare_amt >= 0 && fare_amt < Number(coupon_amt))
                    coupon_amt = fare_amt.toString();
            }
            else {
                coupon_amt = fn_GetTrunc((fare_amt * (coupon_amt / 100)), 2);//10원단위 버림
            }

            if (coupon_amt > 0) {
                if (coupon[9] == "T") {
                    coupon_amt = Number(coupon_amt) + Number(down_fuel_amt);
                }
                trCoupon_Line1.style.display = "inline";
                trCoupon_Line2.style.display = "inline";
                tdCoupon_Amt.innerHTML = "-" + fn_InsertComma(coupon_amt) + "원";
            }
            else {
                trCoupon_Line1.style.display = "none";
                trCoupon_Line2.style.display = "none";
                tdCoupon_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
            }
        }
        else {
            trCoupon_Line1.style.display = "none";
            trCoupon_Line2.style.display = "none";
            tdCoupon_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
        }
        fn_PurchaseSum();
    }

    //추가 할인
    function fn_DisplayADiscountAmtLine(checked) {
        var ddlADiscount = GetObj("ddlADiscount");
        var hidSpclAuth = GetObj("hidSpclAuth");
        var tdADiscount_Exp = GetObj("tdADiscount_Exp");
        var tdADiscount_Amt = GetObj("tdADiscount_Amt");
        var tdADiscount_Inf = GetObj("tdADiscount_Inf");
        var trADiscount_Line1 = GetObj("trADiscount_Line1");
        var trADiscount_Line2 = GetObj("trADiscount_Line2");
        var trADiscountComment01 = GetObj("trADiscountComment01");
        var trADiscountComment02 = GetObj("trADiscountComment02");
        var trADiscountComment03 = GetObj("trADiscountComment03");
        var $trADiscountComment04 = $("#trADiscountComment04"); // 2015-01-05 정신철
        var $trADiscountComment05 = $("#trADiscountComment05"); // 2015-02-24 정신철
        var lblADiscountComment01 = GetObj("lblADiscountComment01");
        var lblADiscountComment02 = GetObj("lblADiscountComment02");
        var rdoADiscountIsUse01 = GetObj("rdoADiscountIsUse01");
        var rdoADiscountIsUse02 = GetObj("rdoADiscountIsUse02");
        var hidADiscountInfoOW = GetObj("hidADiscountInfoOW");
        var hidADiscountInfoRT = GetObj("hidADiscountInfoRT");
        var sIndex = ddlADiscount.selectedIndex;
        var isRoundTrip = GetObj("hdnRoundTrip").value;

        var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
        var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
        var isFareDriven = GetObj("hdnIsFareDriven").value == "Y";
        var ow_adult_fare_amt = 0;
        var ow_child_fare_amt = 0;
        var ow_infant_fare_amt = 0;
        var ow_disable_fare_amt = 0;
        var ow_disableSub_fare_amt = 0;
        var ow_etc_fare_amt = 0;
        var rt_adult_fare_amt = 0;
        var rt_child_fare_amt = 0;
        var rt_infant_fare_amt = 0;
        var rt_disable_fare_amt = 0;
        var rt_disableSub_fare_amt = 0;
        var rt_etc_fare_amt = 0;
        var downline_class = fn_GetSelectedValue_Radio("rdo" + downline_id);
        var upline_class = fn_GetSelectedValue_Radio("rdo" + upline_id);

        if (sIndex == 0 && rdoADiscountIsUse01.checked) {
            rdoADiscountIsUse02.checked = true;
            trADiscount_Line1.style.display = "none";
            trADiscount_Line2.style.display = "none";
            trADiscountComment01.style.display = "none";
            trADiscountComment02.style.display = "none";
            trADiscountComment03.style.display = "none";
            $trADiscountComment04.hide(); // 2015-01-05 정신철
            $trADiscountComment05.hide(); // 2015-02-24 정신철
            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").attr("disabled", ""); // 2015-01-05 정신철 체크박스 비활성
            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").parent().hide(); // 2015-01-05 정신철
            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").removeAttr("checked");

            tdADiscount_Exp.innerHTML = "";
            tdADiscount_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
            tdADiscount_Inf.innerHTML = "";
            return;
        }

        //신분에 해당하는 요금 가져오기
        if (m_xmlHTTP != null && m_xmlHTTP.readyState == 4) {
            if (SelectSingleNode(m_xmlHTTP, "NewDataSet/OW")[0] != null) {
                ow_adult_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0;
                ow_child_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/CHILD_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/CHILD_AMT")) : 0;
                ow_infant_fare_amt = 0;
                ow_disable_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/HAND_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/HAND_AMT")) : 0;
                ow_disableSub_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0;
                ow_etc_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/OW/ADULT_AMT")) : 0;
            }

            if (SelectSingleNode(m_xmlHTTP, "NewDataSet/RT")[0] != null) {
                rt_adult_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT")) : 0;
                rt_child_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/CHILD_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/CHILD_AMT")) : 0;
                rt_infant_fare_amt = 0;
                rt_disable_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/HAND_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/HAND_AMT")) : 0;
                rt_disableSub_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT")) : 0;
                rt_etc_fare_amt = SelectSingleNode(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT").length > 0 ? Number(GetXmlNodeValue(m_xmlHTTP, "NewDataSet/RT/ADULT_AMT")) : 0;
            }
        }

        if (checked) {

            var aDisOWValue = hidADiscountInfoOW.value;
            var aDisRTValue = hidADiscountInfoRT.value;
            var comment01 = "";
            var comment02 = "";

            if (aDisOWValue != "") {
                var aDisOWValueArray = aDisOWValue.split("$");
                var aDisOWValueIndex = 0;
                for (var i = 0; i < aDisOWValueArray.length - 1; i++) {
                    if (ddlADiscount.value == aDisOWValueArray[i].split(";")[0]) {
                        aDisOWValueIndex = i;
                        break;
                    }
                }
                aDisOWValue = aDisOWValue.split("$")[aDisOWValueIndex].split(";");
                comment01 = aDisOWValue[8];
                comment02 = aDisOWValue[9];
                trADiscountComment01.style.display = "inline";
                trADiscountComment02.style.display = "inline";
                if (aDisOWValue[0] == "8FM00001" || aDisOWValue[16] == "T") {
                    trADiscountComment03.style.display = "inline";

                    if (aDisOWValue[16] == "T") { // 기업할인 일때
                        $trADiscountComment04.css("display", "inline"); // 2015-01-05 정신철
                        $("#ctl00_ContentPlaceHolder1_lblADiscountComment04").text(aDisOWValue[19]);
                        $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").parent().show(); // 2015-01-05 정신철
                        if (rdoADiscountIsUse01.checked) {
                            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").removeAttr("disabled"); // 2015-01-05 정신철 체크박스 활성
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment01").css("color", "red");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment02").css("color", "red");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment03").css("color", "red");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment04").css("color", "red");
                        }
                        else {

                            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").attr("disabled", ""); // 2015-01-05 정신철 체크박스 비활성
                            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").removeAttr("checked");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment01").css("color", "");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment02").css("color", "");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment03").css("color", "");
                            $("#ctl00_ContentPlaceHolder1_lblADiscountComment04").css("color", "");
                        }
                    }
                    else {  // 기업할인 아닐 때
                        $trADiscountComment04.hide(); // 2015-01-05 정신철
                        $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").parent().hide(); // 2015-01-05 정신철
                        $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").removeAttr("checked");
                    }
                }
                else {
                    trADiscountComment03.style.display = "none";
                    $trADiscountComment04.hide(); // 2015-01-05 정신철
                    $("#ctl00_ContentPlaceHolder1_lblADiscountComment04").text('');
                    $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").parent().hide(); // 2015-01-05 정신철
                    $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").removeAttr("checked");
                }

                if (aDisOWValue[0] == "11JI0001") { // 2015-02-24 정신철 제주도민 할인 문구 추가
                    $trADiscountComment05.css("display", "inline");
                }
                else {
                    $trADiscountComment05.hide();
                }

                lblADiscountComment01.innerHTML = comment01;
                lblADiscountComment02.innerHTML = comment02.ReplaceAll("[COMPANY_NAME]", "").ReplaceAll("\n", "<br/>");
            }
            if (aDisRTValue != "") {
                var aDisRTValueArray = aDisRTValue.split("$");
                var aDisRTValueIndex = 0;
                for (var i = 0; i < aDisRTValueArray.length - 1; i++) {
                    if (ddlADiscount.value == aDisRTValueArray[i].split(";")[0]) {
                        aDisRTValueIndex = i;
                        break;
                    }
                }
                aDisRTValue = aDisRTValue.split("$")[aDisRTValueIndex].split(";");
            }

            if (rdoADiscountIsUse01.checked == true) {
                var Adult = Number(GetObj("hdnAdult").value);
                var Child = Number(GetObj("hdnChild").value);
                var Infant = Number(GetObj("hdnInfant").value);
                var Disable = Number(GetObj("hdnDisable").value);
                var DisableSub = Number(GetObj("hdnDisableSub").value);
                var Etc = Number(GetObj("hdnEtc").value);
                var totDiscountAmt = 0;
                var owAdultAmt = 0;
                var owAdultSum = 0;
                var owChildAmt = 0;
                var owChildSum = 0;
                var owDisableAmt = 0;
                var owDisableSum = 0;
                var owDisableSubAmt = 0;
                var owDisableSubSum = 0;
                var owEtcAmt = 0;
                var owEtcSum = 0;
                var owTotalDisAmt = 0;
                var rtAdultAmt = 0;
                var rtAdultSum = 0;
                var rtChildAmt = 0;
                var rtChildSum = 0;
                var rtDisableAmt = 0;
                var rtDisableSum = 0;
                var rtDisableSubAmt = 0;
                var rtDisableSubSum = 0;
                var rtEtcAmt = 0;
                var rtEtcSum = 0;
                var rtTotalAmt = 0;

                if (isRoundTrip == "true") {
                    //적용 클레스 별 추가할인 적용가능 여부 체크
                    if (aDisOWValue[5] != "A" && aDisOWValue[5] != downline_class) {
                        alert("선택한 운임은 추가할인을 적용할 수 없습니다.");
                        rdoADiscountIsUse02.checked = true;
                        trADiscount_Line1.style.display = "none";
                        trADiscount_Line2.style.display = "none";
                        //trADiscountComment01.style.display = "none";
                        //trADiscountComment02.style.display = "none";
                        tdADiscount_Exp.innerHTML = "";
                        tdADiscount_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
                        tdADiscount_Inf.innerHTML = "";
                        return;
                    }
                    if (aDisRTValue[5] != "A" && aDisRTValue[5] != upline_class) {
                        alert("선택한 운임은 추가할인을 적용할 수 없습니다.");
                        rdoADiscountIsUse02.checked = true;
                        trADiscount_Line1.style.display = "none";
                        trADiscount_Line2.style.display = "none";
                        //trADiscountComment01.style.display = "none";
                        //trADiscountComment02.style.display = "none";
                        tdADiscount_Exp.innerHTML = "";
                        tdADiscount_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
                        tdADiscount_Inf.innerHTML = "";
                        return;
                    }

                    //할인금액
                    var owDiscountAmt = aDisOWValue[13];
                    var rtDiscountAmt = aDisRTValue[13];

                    //소아 할인금액 추가(2014.10.01 김태우)
                    var owDiscountAmtChd = aDisOWValue[18];
                    var rtDiscountAmtChd = aDisRTValue[18];

                    //할인방법별 할인 금액 계산
                    if (aDisOWValue[12] == "A") {   //정액
                        owAdultAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owAdultSum = owAdultAmt * Adult;
                        owDisableAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owDisableSum = owDisableAmt * Disable;
                        owDisableSubAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owDisableSubSum = owDisableSubAmt * DisableSub;
                        owEtcAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owEtcSum = owEtcAmt * Etc;
                    }
                    else {   //정률
                        owAdultAmt = fn_GetTrunc((ow_adult_fare_amt * (owDiscountAmt / 100)), 2);
                        owAdultSum = owAdultAmt * Adult;
                        owDisableAmt = fn_GetTrunc((ow_disable_fare_amt * (owDiscountAmt / 100)), 2);
                        owDisableSum = owDisableAmt * Disable;
                        owDisableSubAmt = fn_GetTrunc((ow_disableSub_fare_amt * (owDiscountAmt / 100)), 2);
                        owDisableSubSum = owDisableSubAmt * DisableSub;
                        owEtcAmt = fn_GetTrunc((ow_etc_fare_amt * (owDiscountAmt / 100)), 2);
                        owEtcSum = owEtcAmt * Etc;
                    }

                    if (aDisRTValue[12] == "A") {   //정액
                        rtAdultAmt = fn_GetTrunc(rtDiscountAmt, 2);
                        rtAdultSum = rtAdultAmt * Adult;
                        rtDisableAmt = fn_GetTrunc(rtDiscountAmt, 2);
                        rtDisableSum = rtDisableAmt * Disable;
                        rtDisableSubAmt = fn_GetTrunc(rtDiscountAmt, 2);
                        rtDisableSubSum = rtDisableSubAmt * DisableSub;
                        rtEtcAmt = fn_GetTrunc(rtDiscountAmt, 2)
                        rtEtcSum = rtEtcAmt * Etc;
                    }
                    else {   //정률
                        rtAdultAmt = fn_GetTrunc((rt_adult_fare_amt * (rtDiscountAmt / 100)), 2);
                        rtAdultSum = rtAdultAmt * Adult;
                        rtDisableAmt = fn_GetTrunc((rt_disable_fare_amt * (rtDiscountAmt / 100)), 2);
                        rtDisableSum = rtDisableAmt * Disable;
                        rtDisableSubAmt = fn_GetTrunc((rt_disableSub_fare_amt * (rtDiscountAmt / 100)), 2)
                        rtDisableSubSum = rtDisableSubAmt * DisableSub;
                        rtEtcAmt = fn_GetTrunc((rt_etc_fare_amt * (rtDiscountAmt / 100)), 2);
                        rtEtcSum = rtEtcAmt * Etc;
                    }

                    //소아 할인방법별 할인 금액 계산 추가(2014.10.01 김태우)
                    if (aDisOWValue[17] == "A") {   //정액
                        owChildAmt = fn_GetTrunc(owDiscountAmtChd, 2)
                        owChildSum = owChildAmt * Child;
                    }
                    else {   //정률
                        owChildAmt = fn_GetTrunc((ow_child_fare_amt * (owDiscountAmtChd / 100)), 2);
                        owChildSum = owChildAmt * Child;
                    }

                    if (aDisRTValue[17] == "A") {   //정액
                        rtChildAmt = fn_GetTrunc(rtDiscountAmtChd, 2);
                        rtChildSum = rtChildAmt * Child;
                    }
                    else {   //정률
                        rtChildAmt = fn_GetTrunc((rt_child_fare_amt * (rtDiscountAmtChd / 100)), 2);
                        rtChildSum = rtChildAmt * Child;
                    }

                    rtTotalAmt = rtAdultSum + rtChildSum + rtDisableSum + rtDisableSubSum + rtEtcSum;
                    owTotalAmt = owAdultSum + owChildSum + owDisableSum + owDisableSubSum + owEtcSum;
                    totDiscountAmt = owTotalAmt + rtTotalAmt;
                }
                else {
                    //적용 클레스 별 추가할인 적용가능 여부 체크
                    if (aDisOWValue[5] != "A" && aDisOWValue[5] != downline_class) {
                        alert("선택한 운임은 추가할인을 적용할 수 없습니다.");
                        rdoADiscountIsUse02.checked = true;
                        trADiscount_Line1.style.display = "none";
                        trADiscount_Line2.style.display = "none";
                        trADiscountComment01.style.display = "none";
                        trADiscountComment02.style.display = "none";
                        trADiscountComment03.style.display = "none";
                        $trADiscountComment04.hide(); // 2015-01-05 정신철
                        $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").parent().hide(); // 2015-01-05 정신철

                        tdADiscount_Exp.innerHTML = "";
                        tdADiscount_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
                        tdADiscount_Inf.innerHTML = "";
                        return;
                    }

                    //할인금액(정률인 경우 할인률 표시)
                    var owDiscountAmt = aDisOWValue[13];

                    //소아 할인금액 추가(2014.10.01 김태우)
                    var owDiscountAmtChd = aDisOWValue[18];

                    if (aDisOWValue[12] == "A") {   //정액
                        owAdultAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owAdultSum = owAdultAmt * Adult;
                        owDisableAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owDisableSum = owDisableAmt * Disable;
                        owDisableSubAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owDisableSubSum = owDisableSubAmt * DisableSub;
                        owEtcAmt = fn_GetTrunc(owDiscountAmt, 2);
                        owEtcSum = owEtcAmt * Etc;
                    }
                    else {   //정률
                        owAdultAmt = fn_GetTrunc((ow_adult_fare_amt * (owDiscountAmt / 100)), 2);
                        owAdultSum = owAdultAmt * Adult;
                        owDisableAmt = fn_GetTrunc((ow_disable_fare_amt * (owDiscountAmt / 100)), 2);
                        owDisableSum = owDisableAmt * Disable;
                        owDisableSubAmt = fn_GetTrunc((ow_disableSub_fare_amt * (owDiscountAmt / 100)), 2);
                        owDisableSubSum = owDisableSubAmt * DisableSub;
                        owEtcAmt = fn_GetTrunc((ow_etc_fare_amt * (owDiscountAmt / 100)), 2);
                        owEtcSum = owEtcAmt * Etc;
                    }

                    //소아 할인방법별 할인 금액 계산 추가(2014.10.01 김태우)
                    if (aDisOWValue[17] == "A") {   //정액
                        owChildAmt = fn_GetTrunc(owDiscountAmtChd, 2);
                        owChildSum = owChildAmt * Child;
                    }
                    else {   //정률
                        owChildAmt = fn_GetTrunc((ow_child_fare_amt * (owDiscountAmtChd / 100)), 2);
                        owChildSum = owChildAmt * Child;
                    }

                    owTotalAmt = owAdultSum + owChildSum + owDisableSum + owDisableSubSum + owEtcSum;
                    totDiscountAmt = owTotalAmt;
                }
                GetObj("hdnAdultFare").value = ow_adult_fare_amt - owAdultAmt;
                GetObj("hdnUpAdultFare").value = rt_adult_fare_amt - rtAdultAmt;
                GetObj("hdnChildFare").value = ow_child_fare_amt - owChildAmt;
                GetObj("hdnUpChildFare").value = rt_child_fare_amt - rtChildAmt;

                //추가할인 금액계산
                tdADiscount_Exp.innerHTML = "";
                tdADiscount_Amt.innerHTML = "-" + fn_InsertComma(totDiscountAmt) + "원";
                tdADiscount_Inf.innerHTML = "";
                tdADiscount_Inf.innerHTML += "(";
                if ((Adult + DisableSub + Etc) > 0) tdADiscount_Inf.innerHTML += "성인 " + (Adult + DisableSub + Etc).toString() + "인";
                if (Child > 0) {
                    if (tdADiscount_Inf.innerHTML.length > 1) tdADiscount_Inf.innerHTML += ", ";
                    tdADiscount_Inf.innerHTML += "소아 " + Child.toString() + "인";
                }
                if (Disable > 0) {
                    if (tdADiscount_Inf.innerHTML.length > 1) tdADiscount_Inf.innerHTML += ", ";
                    tdADiscount_Inf.innerHTML += "장애인 " + Disable.toString() + "인";
                }
                tdADiscount_Inf.innerHTML += ")";
                hidSpclAuth.value = aDisOWValue[0];

                trADiscount_Line1.style.display = "inline";
                trADiscount_Line2.style.display = "inline";

            }
            else {
                GetObj("hdnAdultFare").value = ow_adult_fare_amt;
                GetObj("hdnUpAdultFare").value = rt_adult_fare_amt;
                GetObj("hdnChildFare").value = ow_child_fare_amt;
                GetObj("hdnUpChildFare").value = rt_child_fare_amt;

                trADiscount_Line1.style.display = "none";
                trADiscount_Line2.style.display = "none";
                tdADiscount_Exp.innerHTML = "";
                tdADiscount_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
                tdADiscount_Inf.innerHTML = "";
                hidSpclAuth.value = ddlADiscount.value;
            }
        }
        else {
            GetObj("hdnAdultFare").value = ow_adult_fare_amt;
            GetObj("hdnUpAdultFare").value = rt_adult_fare_amt;
            GetObj("hdnChildFare").value = ow_child_fare_amt;
            GetObj("hdnUpChildFare").value = rt_child_fare_amt;

            trADiscount_Line1.style.display = "none";
            trADiscount_Line2.style.display = "none";
            trADiscountComment01.style.display = "none";
            trADiscountComment02.style.display = "none";
            trADiscountComment03.style.display = "none";
            $trADiscountComment04.hide();// 2015-01-05 정신철
            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").parent().hide(); // 2015-01-05 정신철
            $("#ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree").removeAttr("checked");

            tdADiscount_Exp.innerHTML = "";
            tdADiscount_Amt.innerHTML = "0&nbsp;&nbsp;&nbsp;";
            tdADiscount_Inf.innerHTML = "";
            hidSpclAuth.value = ddlADiscount.value;
            //ddlADiscount.sele
        }
        fn_PurchaseSum();
    }

    function fn_IsMember_Click(e) {
        var src = GetEventToggle(e);
        var src_checked = src.checked;
        var oContainer = GetParent_by_Tag("TABLE", src);
        var tblPassengerList = GetObj("tblPassengerList");
        var pchsAuth = GetObj("hdnAuth").value;
        var isMFAuth = false;
        if (pchsAuth != "") {
            if (pchsAuth.indexOf("MF") > -1)
                isMFAuth = true;
        }

        for (var i = 0; i < tblPassengerList.rows.length; i++) {
            var row = tblPassengerList.rows[i];
            if (row.cells[0].children[0].tagName == "IMG") continue;

            if (fn_Right(row.cells[3].children[0].id, 6) == "Member") {
                if (row.cells[3].children[0].checked) {
                    row.cells[4].children[0].defaultValue = "-성-";
                    row.cells[5].children[0].defaultValue = "-이름-";
                    row.cells[4].children[0].value = row.cells[4].children[0].defaultValue;
                    row.cells[5].children[0].value = row.cells[5].children[0].defaultValue;
                    row.cells[1].children[0].selectedIndex = 0;
                    row.cells[4].children[0].removeAttribute("readOnly");
                    row.cells[5].children[0].removeAttribute("readOnly");
                    row.cells[1].children[0].removeAttribute("disabled");
                    row.cells[3].children[0].checked = false;
                }
            }
        }

        src.checked = src_checked;
        var row = GetParent_by_Tag("TR", src);
        var family_txt = row.cells[4].children[0];
        var given_txt = row.cells[5].children[0];
        var sex_select = row.cells[1].children[0];
        var family_name = GetObj("hdnMem_FamilyName").value;
        var given_name = GetObj("hdnMem_GivenName").value;
        var sex_cd = GetObj("hdnMem_Sex").value;
        if (src_checked) {
            family_txt.value = family_name;
            given_txt.value = given_name;
            sex_select.selectedIndex = sex_cd == "M" ? 0 : 1;
            family_txt.setAttribute("readOnly", "readOnly");
            given_txt.setAttribute("readOnly", "readOnly");
            sex_select.setAttribute("disabled", "disabled");
        }
        else {
            if (isMFAuth) {
                alert("보너스 항공권 쿠폰을 이용한 예매는 회원 본인만 가능 합니다.");
                e.returnValue = false;
                return false;
            }
            family_txt.value = family_txt.defaultValue;
            given_txt.value = given_txt.defaultValue;
            sex_select.selectedIndex = 0;
            family_txt.removeAttribute("readOnly");
            given_txt.removeAttribute("readOnly");
            sex_select.removeAttribute("disabled");
        }
    }

    function fn_FirstPaxName() {
        var tblPassengerList = GetObj("tblPassengerList");
        if (tblPassengerList == false) return;

        for (var i = 0; i < tblPassengerList.rows.length; i++) {
            var row = tblPassengerList.rows[i];
            if (row.cells[0].children[0].tagName == "IMG") continue;
            var gubun_value = row.cells[0].children[0].value;
            if (gubun_value == "Adult") {
                row.cells[3].children[0].click();
                break;
            }
        }
    }

    function fn_FillPaxList(isChangeGubun) {
        isChangeGubun = isChangeGubun ? true : false; // 2014-04-23 정신철 추가

        var tblPassengerListHeader = GetObj("tblPassengerListHeader");
        var tblPassengerList = GetObj("tblPassengerList");
        if (tblPassengerList == false) return;
        var adult = 1, child = 1, infant = 1, disable = 1, disableSub = 1, etc = 1;
        var isCouponUse = GetObj("ddlCoupon").selectedIndex > 0;
        var isGuest = GetObj("hdnRSV_MBR_GB").value == "NP";
        var name = navigator.appName;

        if (isCouponUse) {
            tblPassengerListHeader.rows[0].cells[2].style["display"] = "inline";
            tblPassengerListHeader.rows[0].cells[4].style["width"] = "285px";
        }
        else {
            tblPassengerListHeader.rows[0].cells[2].style["display"] = "none";
            tblPassengerListHeader.rows[0].cells[4].style["width"] = "315px";
        }

        for (var i = 0; i < tblPassengerList.rows.length; i++) {
            var row = tblPassengerList.rows[i];
            if (row.cells[0].children[0].tagName == "IMG") continue;
            var gubun_value = "";
            var hdnDOB_Ignore = row.cells[6].children[4];
            if (hdnDOB_Ignore.value != "changed") {
                gubun_value = row.cells[0].children[0].value;
                row.cells[0].children[1].value = gubun_value;
            }
            else {
                gubun_value = row.cells[0].children[1].value;
                row.cells[0].children[0].value = gubun_value;
            }
            var gubun_text = "";
            switch (gubun_value) {
                case "Adult": gubun_text = " 성인" + (adult++).toString(); break;
                case "Disable": gubun_text = " 장애인" + (disable++).toString(); break;
                case "DisableSub": gubun_text = " 장애인동반" + (disableSub++).toString(); break;
                case "Etc": gubun_text = " 기타할인대상" + (etc++).toString(); break;
                case "Child": gubun_text = " 소아" + (child++).toString(); break;
                case "Infant": gubun_text = " 유아" + (infant++).toString(); break;
                default: break;
            }
            // row.cells[0].childNodes[4].data = gubun_text;
            row.cells[0].childNodes[5].data = gubun_text; // 2014-04-24 정신철 IE외 브라우저에서 구분문자열 중복 표기되 수정
            var isChildren = (gubun_value == "Child" || gubun_value == "Infant");
            var chkIsCoupon = row.cells[2].children[0];
            if (isCouponUse) {
                row.cells[2].style["display"] = "inline";
                row.cells[4].style["width"] = "100px";
                row.cells[5].style["width"] = "184px";
                if (gubun_value != "Infant")
                    chkIsCoupon.removeAttribute("disabled");
                else
                    chkIsCoupon.setAttribute("disabled", "disabled");
            }
            else {
                row.cells[2].style["display"] = "none";
                row.cells[4].style["width"] = "115px";
                row.cells[5].style["width"] = "199px";
                chkIsCoupon.setAttribute("disabled", "disabled");
            }
            var chkIsMember = row.cells[3].children[0];
            //	회원 본인 선택 확인
            if (chkIsMember.checked == true) {
                var txtFamily = row.cells[4].children[0];
                var txtGiven = row.cells[5].children[0];
                var ddlGender = row.cells[1].children[0];
                var family_name = GetObj("hdnMem_FamilyName").value;
                var given_name = GetObj("hdnMem_GivenName").value;
                var gender_cd = GetObj("hdnMem_Sex").value;
                txtFamily.value = family_name;
                txtGiven.value = given_name;
                ddlGender.selectedIndex = gender_cd == "M" ? 0 : 1;
                txtFamily.setAttribute("readOnly", "readOnly");
                txtGiven.setAttribute("readOnly", "readOnly");
                ddlGender.setAttribute("disabled", "disabled");
            }
            var dob_hdn = row.cells[6].children[0];
            var dob_year = row.cells[6].children[1];
            var dob_month = row.cells[6].children[2];
            var dob_day = row.cells[6].children[3];
            var selected_year = fn_Left(dob_hdn.value, 4);

            var today = new Date(2017, (4 -1), 21, 16, 59, 3);
            var this_year = today.getFullYear();
            var this_month = today.getMonth();
            var this_day = today.getDate();

            if (isChangeGubun == false) { // 2014-04-22 정신철 유/소아/성인 구분변경일 경우 초기화 하지 않음
                for (var j = dob_year.options.length - 1; j >= 0; j--) {
                    dob_year.remove(j);
                }
                var targetYearListNumber = gubun_value == "Child" ? 13 : 2; // 2014-04-22 정신철 추가
                for (var crr_year = this_year; crr_year >= this_year - targetYearListNumber; crr_year--) {
                    var option = new Option(crr_year.toString() + "년", crr_year)
                    dob_year.options.add(option);
                    if (selected_year == crr_year) {
                        option.selected = true;
                    }
                }
                dob_month.selectedIndex = this_month;
                dob_day.selectedIndex = this_day - 1;
            }

            if (isChildren) {
                chkIsMember.setAttribute("disabled", "disabled");
                dob_year.style.display = "inline";
                dob_month.style.display = "inline";
                dob_day.style.display = "inline";
            }
            else {
                chkIsMember.removeAttribute("disabled");
                dob_year.style.display = "none";
                dob_month.style.display = "none";
                dob_day.style.display = "none";
            }
            if (isGuest)
                chkIsMember.setAttribute("disabled", "disabled");
        }
    }

    function fn_ddlGroup_Gubun_Change() {
        var txtGroup_Etc = GetObj("ctl00_ContentPlaceHolder1_txtGroup_Etc");
        var Group_Gubun = GetObj("ctl00_ContentPlaceHolder1_ddlGroup_Gubun");
        var ddlNation = GetObj("ctl00_ContentPlaceHolder1_ddlNation");
        if (Group_Gubun.value == "IB") {
            ddlNation.style["display"] = "block";
        }
        else {
            ddlNation.style["display"] = "none";
        }
    }

    function fn_Validation_Group() {
        var isRsvProgress = false;
        var tdValidationInfo = GetObj("ctl00_ContentPlaceHolder1_tdValidationInfo");
        tdValidationInfo.innerHTML = "&nbsp;";
        var focus_control = null;
        var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
        var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
        var isRoundTrip = GetObj("hdnRoundTrip").value != "false";
        var message_text = "";
        var isValid = true;
        var downline_class = fn_GetSelectedValue_Radio("rdo" + downline_id);
        var upline_class = fn_GetSelectedValue_Radio("rdo" + upline_id);
        var Group_Gubun = GetObj("ctl00_ContentPlaceHolder1_ddlGroup_Gubun");
        var ddlNation = GetObj("ctl00_ContentPlaceHolder1_ddlNation");

        //	운임규정에 동의
        if (GetObj("ctl00_ContentPlaceHolder1_hdnMEM_CLASS").value != "G" && GetObj("chkPayAgree").checked != true) {
            message_text += "\r\n전자결제서비스 이용약관에 동의하지 않으셨습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("chkPayAgree");
            isValid = false;
        }

        //	운임규정에 동의
        if (GetObj("chkAgree").checked != true) {
            message_text += "\r\n운임규정에 동의하지 않으셨습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("chkAgree");
            isValid = false;
        }
        //인바운드 단체일 경우 : 국적선택 확인
        if (Group_Gubun.value == "IB") {
            if (ddlNation.value == "") {
                message_text += "\r\n국적을 선택해 주십시오.";
                isValid = false;
            }
        }

        if (isRoundTrip) { //왕복인 경우
            if (downline_class == "" || upline_class == "") {
                message_text += "\r\n운임을 선택하지 않으셨습니다. 만일 모두 매진이라면 이전날, 다음날을 조회하실 수도 있습니다.";
                isValid = false;
            }

            //	가는날이 오는날 보다 과거인지 확인
            var down_date = GetObj(downline_id + "_hdnDate").value;
            var up_date = GetObj(upline_id + "_hdnDate").value;

            var down_visible = GetObj(downline_id + "_hdnVisible").value != "false";
            var up_visible = GetObj(upline_id + "_hdnVisible").value != "false";
            var down_dept_arrt = GetObj(downline_id + "_hdnDEPT_ARRT").value;
            var up_dept_arrt = GetObj(upline_id + "_hdnDEPT_ARRT").value;
            var arr_down_dept_arrt = down_dept_arrt.split("-");
            var arr_up_dept_arrt = up_dept_arrt.split("-");
            if ((down_visible && up_visible) && down_date > up_date) {
                message_text += "\r\n오는날이 가는날보다 더 빠릅니다.";
                isValid = false;
            }
                //	같은 날일 때 오는 편의 출발시간이 가는 편의 도착시간보다 빠른지 확인.
            else if ((down_visible && up_visible) && (!IsEmpty(down_dept_arrt) && !IsEmpty(up_dept_arrt)) && (arr_down_dept_arrt != null && arr_down_dept_arrt.length > 1) && (arr_up_dept_arrt != null && arr_up_dept_arrt.length > 1)) {
                var down_arr_dt = fn_GetFlightDateTime(down_date, arr_down_dept_arrt[1]);
                var up_dep_dt = fn_GetFlightDateTime(up_date, arr_up_dept_arrt[0]);
                var add_hour = up_dep_dt.getTime() - (60 * 60000);	//	1시간을 뺀다.
                var trans_added_dt = new Date(2017, (4 -1), 21, 16, 59, 3);
                trans_added_dt.setTime(add_hour);
                if (down_arr_dt > up_dep_dt) {
                    message_text += "\r\n오는편의 출발시간이 가는편의 도착시간보다 더 빠릅니다.";
                    isValid = false;
                }
                else if (down_arr_dt <= up_dep_dt && down_arr_dt > trans_added_dt) {
                    message_text += "\r\n가는편 도착 후 오는편을 타기 위한 시간이 너무 짧습니다.";
                    isValid = false;
                }
            }
    }
    else { //편도인 경우
        if (downline_class == "") {
            message_text += "\r\n운임을 선택하지 않으셨습니다. 만일 모두 매진이라면 이전날, 다음날을 조회하실 수도 있습니다.";
            isValid = false;
        }
    }
        //	단체일 경우 단체 설명 입력 확인
    if (IsEmpty(GetObj("ctl00_ContentPlaceHolder1_txtGroup_Etc").value)) {
            message_text += "\r\n그룹 이름을 입력하여 주십시오.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtGroup_Etc");
            isValid = false;
        }
        //	기타 단체일 경우 단체 설명에 특수문자 입력 불허
        var pattern = /[\~\`\!\@\#\$\%\^\&\*\(\)\-\_\+\=\{\}\[\]\\\|\;\:\"\'\<\,\>\.\?\/]/
        if (pattern.test(GetObj("ctl00_ContentPlaceHolder1_txtGroup_Etc").value)) {
            message_text += "\r\n그룹수요 성격에는 특수문자를 입력하실 수 없습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtGroup_Etc");
            isValid = false;
        }

        if (!IsEmpty(GetObj("ctl00_ContentPlaceHolder1_txtMobile").value) && GetObj("ctl00_ContentPlaceHolder1_txtMobile").value.length < 10) {
            message_text += "\r\n휴대폰 번호가 유효하지 않습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtMobile");
            isValid = false;
        }
        else if (!IsEmpty(GetObj("ctl00_ContentPlaceHolder1_txtMobile").value) && !checkMobile(GetObj("ctl00_ContentPlaceHolder1_txtMobile").value)) {
                message_text += "\r\n휴대폰 번호가 유효하지 않습니다.";
                focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtMobile");
                isValid = false;
            }
        //	이메일 확인
        var email = GetObj("ctl00_ContentPlaceHolder1_txtEmail").value;
        if (IsEmpty(email)) {
            message_text += "\r\n이메일 주소를 입력하지 않으셨습니다.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtEmail");
            isValid = false;
        }
            //	이메일 형식 확인
        else if (!IsEmpty(email) && !email.IsEmail()) {
            message_text += "\r\n이메일 주소를 (xxx@sample.com)와 같은 형식으로 입력하세요.";
            focus_control = focus_control != null ? focus_control : GetObj("ctl00_ContentPlaceHolder1_txtEmail");
            isValid = false;
        }
        //	메시지 띄우기
    if (!isValid) {
        if (message_text != "") {
            tdValidationInfo.innerHTML = fn_GetHTML_MessageBox(message_text);	//	message_text.Trim().ReplaceAll("\r\n", "<br />");
        }
        if (focus_control != null) {
            focus_control.focus();
            if (focus_control.select)
                focus_control.select();
        }
        return false;
    }

    var msg = "";
    if (downline_class == "E" || upline_class == "E") {
        msg = "〈 환불 위약금 안내 〉\n\n";
        msg += "출발 60일전 ~ 31일전 : 편도 1인당 1천원 \n";
        msg += "출발 30일전 ~ 출발 8일전 : 편도 1인당 2천원\n";
        msg += "출발 7일전 ~ 출발 2일전 : 편도 1인당 3천원\n";
        msg += "출발 1일전 ~ 출발시간 : 편도 1인당 8천원\n";
        msg += "출발 예정시간 이후 : 편도 1인당 1만 2천원\n";
        msg += "(최초 예매 당일에는 위약금이 면제 됩니다.)\n\n\n";
        msg += "예매하시겠습니까?";
    }
    else if (downline_class == "Y" && upline_class == "Y") {
        msg = "〈 환불 위약금 안내 〉\n\n";
        msg += "출발 60일전 ~ 31일전 : 편도 1인당 1천원 \n";
        msg += "출발 30일전 ~ 출발 8일전 : 편도 1인당 2천원\n";
        msg += "출발 7일전 ~ 출발 2일전 : 편도 1인당 3천원\n";
        msg += "출발 1일전 ~ 출발시간 : 편도 1인당 8천원\n";
        msg += "출발 예정시간 이후 : 편도 1인당 1만 2천원\n";
        msg += "(최초 예매 당일에는 위약금이 면제 됩니다.)\n\n\n";
        msg += "예매하시겠습니까?";
    }
    else if (downline_class == "G" || upline_class == "G") {
        msg = "〈 환불 위약금 안내 〉\n\n";
        msg += "출발 60일전 ~ 31일전 : 편도 1인당 1천원 \n";
        msg += "출발 30일전 ~ 출발 8일전 : 편도 1인당 2천원\n";
        msg += "출발 7일전 ~ 출발 2일전 : 편도 1인당 3천원\n";
        msg += "출발 1일전 ~ 출발시간 : 편도 1인당 8천원\n";
        msg += "출발 예정시간 이후 : 편도 1인당 1만 2천원\n";
        msg += "(최초 예매 당일에는 위약금이 면제 됩니다.)\n\n\n";
        msg += "예매하시겠습니까?";
    }

    var result = isValid && fn_OpenConfirm("", msg);
    if (result) {
        if (isRsvProgress == false) {
            ProgressBar("purchase");
            RequestReservation() // 기존 fn_RequestReservation();
            isRsvProgress = true;
        }
        else {
            alert("예약 진행중 입니다.");
        }
    }
    return false;
}

function fn_GoScheduleSelect() {
    if (fn_OpenConfirm("", "이전 페이지로 이동하면 일정선택부터 다시 하셔야 합니다.\r\n이전 페이지로 이동하시겠습니까?")) {
        return true;
    }
    return false;
}

function fn_Valid_UpDown_Date(fltlst_id, add_day) {
    //소아단독발권시 동반인 체크 이후 다른여정을 조회할 경우 Y값을 제거해준다
    if (GetObj("ctl00_ContentPlaceHolder1_hdnOnlyChild").value == "Y")
        GetObj("ctl00_ContentPlaceHolder1_hdnOnlyChild").value = "";

    var isValid = true;
    var message_text = "";
    var isFormer_Compare = false;
    var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
    var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
    var compare_date = GetDate(GetObj(fltlst_id + "_hdnDate").value);
    var date_min = new Date(2017, (4 -1), 21, 16, 59, 3);
        var isRoundTrip = GetObj("hdnRoundTrip").value != "false";
        date_min = new Date(date_min.getFullYear(), date_min.getMonth(), date_min.getDate());
        var date_max = new Date(2017, (4 -1), 21, 16, 59, 3);
        date_max = new Date(date_max.getFullYear(), date_max.getMonth(), date_max.getDate());
        var ms = date_max.getTime() + (240 * 24 * 60 * 60 * 1000);
        date_max.setTime(ms);
    //var date_max = new Date(2014, 2, 30);

        compare_date.setTime(compare_date.getTime() + (add_day * 24 * 60 * 60 * 1000));

        if (isValid) {

            if (GetObj(downline_id + "_hdnFormerFareYN").value == "Y") {
                date_min = GetDate(GetObj(downline_id + "_hdnDate").value);
                isFormer_Compare = true;
            }
            else if (GetObj(upline_id + "_hdnFormerFareYN").value == "Y") {
                date_max = GetDate(GetObj(upline_id + "_hdnDate").value);
                isFormer_Compare = true;
            }

            if (add_day > 0) {
                if (fltlst_id == downline_id && isRoundTrip && GetObj(downline_id + "_hdnVisible").value == "true" && GetDate(GetObj(upline_id + "_hdnDate").value) < compare_date) {
                    isValid = false;
                    message_text = "오는날 이후의 날짜를 선택할 수 없습니다.";
                }
                else if (date_max <= compare_date) {
                    isValid = false;
                    if (isFormer_Compare) {
                        message_text = "오는날 이후의 날짜를 선택할 수 없습니다.";
                    }
                    else {
                        message_text = "오늘로부터 240일 이후 날짜를 선택할 수 없습니다.";
                    }
                }
            }
            else if (add_day < 0) {
                if (fltlst_id == upline_id && isRoundTrip && GetObj(upline_id + "_hdnVisible").value == "true" && GetDate(GetObj(downline_id + "_hdnDate").value) > compare_date) {
                    isValid = false;
                    message_text = "가는날 이전의 날짜를 선택할 수 없습니다.";
                }
                else if (date_min > compare_date) {
                    isValid = false;
                    if (isFormer_Compare) {
                        message_text = "가는날 이전의 날짜를 선택할 수 없습니다.";
                    }
                    else {
                        message_text = "이전 날짜를 선택할 수 없습니다.";
                    }
                }
            }
        }

        if (!IsEmpty(message_text)) {
            alert(message_text);
        }

    //	debugger
        if (isValid) {
            fn_GetNormalFare(fltlst_id, add_day);
        }
        return false;
}

function fn_Valid_UpDown_DateforChild(fltlst_id, add_day) {
            //소아단독발권시 동반인 체크 이후 다른여정을 조회할 경우 Y값을 제거해준다
            if (GetObj("ctl00_ContentPlaceHolder1_hdnOnlyChild").value == "Y")
                GetObj("ctl00_ContentPlaceHolder1_hdnOnlyChild").value = "";

    var isValid = true;
    var message_text = "";
    var isFormer_Compare = false;
    var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
    var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
            var compare_date = GetDate(GetObj(fltlst_id + "_hdnDate").value);
            var date_min = new Date(2017, (4 -1), 21, 16, 59, 3);
    var isRoundTrip = GetObj("hdnRoundTrip").value != "false";
    date_min = new Date(date_min.getFullYear(), date_min.getMonth(), date_min.getDate());
    var date_max = new Date(2017, (4 -1), 21, 16, 59, 3);
        date_max = new Date(date_max.getFullYear(), date_max.getMonth(), date_max.getDate());
        var ms = date_max.getTime() + (240 * 24 * 60 * 60 * 1000);
        date_max.setTime(ms);
            //var date_max = new Date(2014, 2, 30);

        compare_date.setTime(compare_date.getTime() + (add_day * 24 * 60 * 60 * 1000));

        if (isValid) {

            if (GetObj(downline_id + "_hdnFormerFareYN").value == "Y") {
                date_min = GetDate(GetObj(downline_id + "_hdnDate").value);
                isFormer_Compare = true;
            }
            else if (GetObj(upline_id + "_hdnFormerFareYN").value == "Y") {
                date_max = GetDate(GetObj(upline_id + "_hdnDate").value);
                isFormer_Compare = true;
            }

            if (add_day > 0) {
                if (fltlst_id == downline_id && isRoundTrip && GetObj(downline_id + "_hdnVisible").value == "true" && GetDate(GetObj(upline_id + "_hdnDate").value) < compare_date) {
                    isValid = false;
                    message_text = "오는날 이후의 날짜를 선택할 수 없습니다.";
                }
                else if (date_max <= compare_date) {
                    isValid = false;
                    if (isFormer_Compare) {
                        message_text = "오는날 이후의 날짜를 선택할 수 없습니다.";
                    }
                    else {
                        message_text = "오늘로부터 240일 이후 날짜를 선택할 수 없습니다.";
                    }
                }
            }
            else if (add_day < 0) {
                if (fltlst_id == upline_id && isRoundTrip && GetObj(upline_id + "_hdnVisible").value == "true" && GetDate(GetObj(downline_id + "_hdnDate").value) > compare_date) {
                    isValid = false;
                    message_text = "가는날 이전의 날짜를 선택할 수 없습니다.";
                }
                else if (date_min > compare_date) {
                    isValid = false;
                    if (isFormer_Compare) {
                        message_text = "가는날 이전의 날짜를 선택할 수 없습니다.";
                    }
                    else {
                        message_text = "이전 날짜를 선택할 수 없습니다.";
                    }
                }
            }
        }

        if (!IsEmpty(message_text)) {
            alert(message_text);
        }

            //	debugger
        if (isValid) {
            fn_GetChildFare(fltlst_id, add_day);
        }
        return false;
    }

    function fn_ddlCoupon_Change(e) {
        var chkPoint = GetObj("chkPoint");
        var ddlCoupon = GetEventToggle(e);

        if (chkPoint.checked == true && ddlCoupon.selectedIndex > 0) {
            fn_OpenInformation("", "쿠폰, 수수료 적용을 중복으로 적용할 수 없습니다.");
            ddlCoupon.selectedIndex = 0;
        }
        else {
            var lblCouponText = GetObj("lblCouponText");
            var isCouponUse = ddlCoupon.selectedIndex > 0;
            var coupon = ddlCoupon.value.split("|");
            var trCouponComment2 = GetObj("trCouponComment2");
            var trCouponComment3 = GetObj("trCouponComment3");

            //	쿠폰 유효성 확인
            if (isCouponUse) {
                //	적용편의 탑승일자가 유효한지 확인
                if (!fn_Valid_Coupon()) {
                    var message_text = "선택하신 쿠폰 '" + ddlCoupon.options[ddlCoupon.selectedIndex].text + "'은 "; // + coupon[5] + "→" + coupon[6] + " 구간에 대해서\r\n";
                    message_text += GetDateText(coupon[2]) + " ~ " + GetDateText(coupon[3]) + " 사이에 탑승하시는 비행편에만 적용됩니다.";
                    alert(message_text);
                    ddlCoupon.selectedIndex = 0;
                    isCouponUse = false;
                }

                //쿠폰이 EMBARGO 기간에 포함되었는지
                if (fn_Valid_Embargo()) {
                    var message_text = "쿠폰 성수기 기간으로 쿠폰 이용이 불가능입니다.\n(" + embargo_range + ")";
                    alert(message_text);
                    ddlCoupon.selectedIndex = 0;
                    isCouponUse = false;
                }
            }
            if (isCouponUse) {
                lblCouponText.innerHTML = GetDateText(coupon[2]) + "~" + GetDateText(coupon[3]);
                if (coupon[9] == "T") {
                    lblCouponText.innerHTML += "(유류할증포함)"
                }
                trCouponComment2.style.display = "inline";
                trCouponComment3.style.display = "inline";
            }
            else {
                lblCouponText.innerHTML = "";
                trCouponComment2.style.display = "none";
                trCouponComment3.style.display = "none";
            }
            var tblPassengerList = GetObj("tblPassengerList");
            if (tblPassengerList == false) return;
            for (var i = 0; i < tblPassengerList.rows.length; i++) {
                var row = tblPassengerList.rows[i];
                if (row.cells[0].children[0].tagName == "IMG") continue;
                var chkIsCoupon = row.cells[2].children[0];
                chkIsCoupon.checked = false;
                if (isCouponUse) {
                    var pax_gubun = row.cells[0].children[0].value;
                    if (pax_gubun != "Infant")
                        chkIsCoupon.removeAttribute("disabled");
                    else
                        chkIsCoupon.setAttribute("disabled", "disabled");
                }
                else {
                    chkIsCoupon.setAttribute("disabled", "disabled");
                }
            }
            fn_DisplayCouponAmtLine(false);
            fn_FillPaxList();
        }
    }

    function fn_Valid_Coupon() {
        var isValid = false;
        var ddlCoupon = GetObj("ddlCoupon");
        if (ddlCoupon.selectedIndex <= 0) return false;
        var coupon = ddlCoupon.value.split("|");
        var compare_date = "";
        var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
        var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";

        if (coupon[4] == "가는편") {
            compare_date = GetObj(downline_id + "_hdnDate").value;
        }
        else if (coupon[4] == "오는편") {
            compare_date = GetObj(upline_id + "_hdnDate").value;
        }
        else {//모든 구간 적용인 경우 가는편의 날짜 기준
            compare_date = GetObj(downline_id + "_hdnDate").value;
        }
        //	적용편의 탑승일자가 유효한지 확인
        if (coupon[2] <= compare_date && compare_date <= coupon[3]) {
            isValid = true;
        }
        else {
            isValid = false;
        }
        return isValid;
    }

    function fn_ddlADiscount_Change() {
        $("#ctl00_ContentPlaceHolder1_lblADiscountComment01").css("color", "");
        $("#ctl00_ContentPlaceHolder1_lblADiscountComment02").css("color", "");
        $("#ctl00_ContentPlaceHolder1_lblADiscountComment03").css("color", "");
        $("#ctl00_ContentPlaceHolder1_lblADiscountComment04").css("color", "");

        var chkPoint = GetObj("chkPoint");
        var ddlADiscount = GetObj("ddlADiscount");
        var rdoADiscountIsUse01 = GetObj("rdoADiscountIsUse01");
        var rdoADiscountIsUse02 = GetObj("rdoADiscountIsUse02");

        if (chkPoint.checked == true && ddlADiscount.selectedIndex > 0 && rdoADiscountIsUse01.checked) {
            fn_OpenInformation("", "추가할인, 수수료 적용을 중복으로 적용할 수 없습니다.");
            ddlADiscount.selectedIndex = 0;
            rdoADiscountIsUse01.checked = false;
            rdoADiscountIsUse02.checked = true;
        }
        else {
            var isADiscountUse = ddlADiscount.selectedIndex > 0;
            fn_DisplayADiscountAmtLine(isADiscountUse);
        }
    }

    var embargo_range;

    function fn_Valid_Embargo() {
        var isValid = false;
        var ddlCoupon = GetObj("ddlCoupon");
        if (ddlCoupon.selectedIndex <= 0) return false;

        var coupon = ddlCoupon.value.split("|");
        var compare_date = "";
        var downline_id = "ctl00_ContentPlaceHolder1_fltlstDownLine";
        var upline_id = "ctl00_ContentPlaceHolder1_fltlstUpLine";
        if (coupon[4] == "가는편") {
            compare_date = GetObj(downline_id + "_hdnDate").value;
        }
        else if (coupon[4] == "오는편") {
            compare_date = GetObj(upline_id + "_hdnDate").value;
        }
        //쿠폰이 EMBARGO 적용이 되어 있다면
        if (coupon[8] == "T") {
            var embargo = GetObj("hdnEmbargo");
            if (!IsEmpty(embargo)) {
                var embargoAr = embargo.value.Trim().split('|');
                for (var i = 0; i < embargoAr.length - 1 ; i++) {
                    var embargoUnit = embargoAr[i].split('-');
                    if (embargoUnit[0] <= compare_date && compare_date <= embargoUnit[1]) {
                        embargo_range = embargoUnit[0].substring(0, 4) + "년 " + embargoUnit[0].substring(4, 6) + "월 " + embargoUnit[0].substring(6, 8) + "일 ~ " + embargoUnit[1].substring(0, 4) + "년 " + embargoUnit[1].substring(4, 6) + "월 " + embargoUnit[1].substring(6, 8) + "일";
                        isValid = true;
                        break;
                    }
                }
            }
        }
        return isValid;
    }

    function fn_Valid_EngKor_Name(name) {
        var isValid = true;
        if (!IsEmpty(name)) {
            var isEng = false;
            var isKor = false;
            for (var i = name.length - 1; i >= 0; i--) {
                var char_code = name.charCodeAt(i);
                if ((65 <= char_code && char_code <= 90) || (97 <= char_code && char_code <= 122)) {
                    isEng = isEng || true;
                }
                else if (!((48 <= char_code && char_code <= 57) || (96 <= char_code && char_code <= 111) || (186 < char_code && char_code < 222))) {
                    isKor = isKor || true;
                }
            }
            isValid = (isEng ^ isKor);
        }
        return isValid;
    }

    function fn_Name_Keydown(e) {
        var evt = window.event || e;
        var keycode = evt.keyCode;
        if ((48 <= keycode && keycode <= 57) || (96 <= keycode && keycode <= 111) || (186 < keycode && keycode < 222)) {
            event.returnValue = false;
        }
    }

    function fn_Name_Change(e) {
        var evt = window.event || e;
        var textbox = GetEventToggle(evt);
        var text = textbox.value.toString();
        for (var i = text.length - 1; i >= 0; i--) {
            var char_code = text.charCodeAt(i);
            if ((0 <= char_code && char_code <= 64) || (91 <= char_code && char_code <= 96) || (123 <= char_code && char_code <= 126)) {
                text = fn_Left(text, i) + fn_Right(text, text.length - i - 1);
            }
        }
        textbox.value = text;
    }

    function fn_Textbox_Enter(field) {
        if (field.readOnly != null && field.readOnly == true) {
            return false;
        }
        if (field.value == field.defaultValue) {
            field.value = "";
        }
    }

    function fn_Textbox_Exit(field) {
        if (field.value == "") {
            field.value = field.defaultValue;
        }
    }

    function openSettieError() {
        var sURL = "PUsettleError.html";
        fn_OpenWindow(sURL, "PUsettleError", "600", "665", "no");
    }

    function openCertInfo() {
        var sURL = "PUCertificate.html";
        fn_OpenWindow(sURL, "PUCertificate", "720", "850", "yes");
    }

    function fn_SeatCntView(cnt, acType, e) {
        var evt = window.event || e;
        var DivRef = document.getElementById('divSeatCnt');
        var divCnt = document.getElementById('divCnt');

        if (cnt > 0) {
            divCnt.innerHTML = cnt + "석 / 기종:B" + acType;
            DivRef.style.display = "block";
            DivRef.style.top = document.body.scrollTop + evt.clientY - 10;
            DivRef.style.left = document.body.scrollLeft + evt.clientX + 10;
        }
    }

    function fn_SeatCntHide() {
        var DivRef = document.getElementById('divSeatCnt');
        DivRef.style.display = "none";
    }

    function SetAccountType() {
        if (GetObj("ctl00_ContentPlaceHolder1_rdoCard").checked) {
            GetObj("tbCard").style["display"] = "inline";
            GetObj("tbPrivateCard").style["display"] = "none";
            GetObj("tbBankPay").style["display"] = "none";
            GetObj("tbKakaoPay").style["display"] = "none";
            GetObj("tbCash").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_trTerm").style["display"] = "inline";
            GetObj("ctl00_ContentPlaceHolder1_pnlPayAgree").style["display"] = "inline";
            GetObj("ctl00_ContentPlaceHolder1_pnlTerms").style["display"] = "inline";
        }
        else if (GetObj("ctl00_ContentPlaceHolder1_rdoPrivateCard").checked) {
            GetObj("tbCard").style["display"] = "none";
            GetObj("tbPrivateCard").style["display"] = "inline";
            GetObj("tbBankPay").style["display"] = "none";
            GetObj("tbKakaoPay").style["display"] = "none";
            GetObj("tbCash").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_trTerm").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlPayAgree").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlTerms").style["display"] = "none";
        }
        else if (GetObj("ctl00_ContentPlaceHolder1_rdoBank").checked) {
            GetObj("tbCard").style["display"] = "none";
            GetObj("tbPrivateCard").style["display"] = "none";
            GetObj("tbBankPay").style["display"] = "inline";
            GetObj("tbKakaoPay").style["display"] = "none";
            GetObj("tbCash").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_trTerm").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlPayAgree").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlTerms").style["display"] = "none";
        }
        else if (GetObj("ctl00_ContentPlaceHolder1_rdoKKAO").checked) {
            GetObj("tbCard").style["display"] = "none";
            GetObj("tbPrivateCard").style["display"] = "none";
            GetObj("tbBankPay").style["display"] = "none";
            GetObj("tbKakaoPay").style["display"] = "inline";
            GetObj("tbCash").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_trTerm").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlPayAgree").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlTerms").style["display"] = "none";
        }
        else if (GetObj("ctl00_ContentPlaceHolder1_rdoCash").checked) {
            GetObj("tbCard").style["display"] = "none";
            GetObj("tbPrivateCard").style["display"] = "none";
            GetObj("tbBankPay").style["display"] = "none";
            GetObj("tbKakaoPay").style["display"] = "none";
            GetObj("tbCash").style["display"] = "inline";
            GetObj("ctl00_ContentPlaceHolder1_trTerm").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlPayAgree").style["display"] = "none";
            GetObj("ctl00_ContentPlaceHolder1_pnlTerms").style["display"] = "none";
        }
}

function fn_NextFocus(control1, control2, len) {
    if (GetObj(control1).value.length >= len) {
        GetObj(control2).focus();
    }
}

function BadMemberPopup(MbrNo) {
    fn_OpenModaless('/User/BadMemberPopup.aspx?MbrNo=' + MbrNo, 'BadMember', '700', '400', 'yes');
    return false;
}

function ClickBtnApproval() {
    if (GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked == true) {
        var ddlCoupon = GetObj("ddlCoupon");
        var ddlADiscount = GetObj("ddlADiscount");
        var rdoADiscountIsUse01 = GetObj("rdoADiscountIsUse01");

        if (ddlCoupon.selectedIndex > 0 || (ddlADiscount.selectedIndex > 0 && rdoADiscountIsUse01.checked)) {
            fn_OpenInformation("", "쿠폰, 추가할인을 중복으로 적용할 수 없습니다.");
            GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
            GetObj("tdPoint").innerHTML = "";
            GetObj("tbPoint").style["display"] = "none";
        }
        else {
            var agent_cd = "";
            var request_xml = "<REQUEST><TASK>AgentRemainPoint</TASK>";
            request_xml += "<AGENT_CD>" + agent_cd + "</AGENT_CD>";
            request_xml += "</REQUEST>";

            RequestHTTP(request_xml, RequestClickBtnApproval, null);
        }
    }
    else
        fn_Validation();
}

function ClickChkPoint() {
    if (GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked == true) {
        var ddlCoupon = GetObj("ddlCoupon");
        var ddlADiscount = GetObj("ddlADiscount");
        var rdoADiscountIsUse01 = GetObj("rdoADiscountIsUse01");

        if (ddlCoupon.selectedIndex > 0 || (ddlADiscount.selectedIndex > 0 && rdoADiscountIsUse01.checked)) {
            fn_OpenInformation("", "쿠폰, 추가할인을 중복으로 적용할 수 없습니다.");
            GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
            GetObj("tdPoint").innerHTML = "";
            GetObj("tbPoint").style["display"] = "none";
        }
        else {
            var agent_cd = "";
            var request_xml = "<REQUEST><TASK>AgentRemainPoint</TASK>";
            request_xml += "<AGENT_CD>" + agent_cd + "</AGENT_CD>";
            request_xml += "</REQUEST>";

            RequestHTTP(request_xml, RequestClickChkPoint, null);
        }
    }
    else {
        ShowDivBackgroud(); // 투명 Div 띄우기
        fn_OpenLayer("divPointCancel", 280, 250);
    }
}

function RequestClickBtnApproval() {
    if (m_xmlHTTP != null && m_xmlHTTP.readyState == 4) {
        if (GetXmlNodeValue(m_xmlHTTP, "RESULT/REMAIN_POINT") != null) {
            var remainPoint = GetXmlNodeValue(m_xmlHTTP, "RESULT/REMAIN_POINT");
            var purchaseAmt = fn_GetValue("tdPurchase");

            if (remainPoint >= purchaseAmt)
                fn_Validation();
            else {
                GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
                var msg = "잔여 수수료가 부족합니다.(잔여:" + fn_InsertComma(remainPoint) + "원/필요:" + fn_InsertComma(purchaseAmt) + "원/부족:" + fn_InsertComma(purchaseAmt - remainPoint) + "원)";
                fn_OpenInformation("", msg);
            }
        }
        else {
            fn_OpenInformation("", "잔여 수수료가 부족합니다.");
            GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
        }
    }
}

function RequestClickChkPoint() {
    if (m_xmlHTTP != null && m_xmlHTTP.readyState == 4) {
        if (GetXmlNodeValue(m_xmlHTTP, "RESULT/REMAIN_POINT") != null) {
            var remainPoint = GetXmlNodeValue(m_xmlHTTP, "RESULT/REMAIN_POINT");
            SetPointUseLayer(remainPoint); // 화면에 표시될 팝업 설정                                                                                                    
        }
        else {
            fn_OpenInformation("", "잔여 수수료가 부족합니다.");
            GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
        }
    }
}

function ShowDivBackgroud() {
    var screenWidth = 0;
    var screenHeight = 0;

    if (BrowserDetect.browser == "Firefox") {
        // FireFox
        screenWidth = document.body.scrollWidth;
        screenHeight = document.body.scrollHeight;
    }
    else {
        // IE, Safari, Chrome(IE 기준임)
        screenWidth = window.screen.width - 22; // IE 에서 22를 빼줘야 가로 스크롤이 안생김	            	            
        screenHeight = (window.screen.height * 2); -window.screen.availHeight;
    }

    // Position 0,0으로 이동
    window.scrollTo(0, 0);
    // 화면에 표시될 배경 Div 설정
    GetObj("divBackgroud").style.top = 0;
    GetObj("divBackgroud").style.left = 0;
    GetObj("divBackgroud").style.width = screenWidth;
    GetObj("divBackgroud").style.height = screenHeight;
    GetObj("divBackgroud").style.display = "";

    GetObj("divBackgroud").style.backgroundColor = "gray";
    GetObj("divBackgroud").style.opacity = "0.5";
    GetObj("divBackgroud").style.filter = "alpha(opacity=50)";
}

// 포인트 사용 DIV(버튼 클릭)
function PointUseDiv(arg) {
    GetObj("divBackgroud").style.display = "none";
    GetObj("divPointUse").style.display = "none";
    jQuery(".popup-backdrop").remove();

    if (arg == "Y")
        GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = true;
    else
        GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;

    SetTotalAmt();
}

// 포인트 취소 DIV(버튼 클릭)
function PointCancelDiv(arg) {
    GetObj("divBackgroud").style.display = "none";
    GetObj("divPointCancel").style.display = "none";
    jQuery(".popup-backdrop").remove();

    if (arg == "Y") {
        GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
        var evt = window.event;
        fn_SetSummaryText(evt);
    }
    else
        GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = true;

    SetTotalAmt();
}

function SetPointUseLayer(remainPoint) {
    var adultPax = Number(GetObj("hdnAdult").value);
    var disablePax = Number(GetObj("hdnDisable").value);
    var disableSubPax = Number(GetObj("hdnDisableSub").value);
    var etcPax = Number(GetObj("hdnEtc").value);
    var childPax = Number(GetObj("hdnChild").value);

    var adultFareOW = GetObj("ctl00_ContentPlaceHolder1_hdnAdultFare").value;
    var adultFareRT = GetObj("ctl00_ContentPlaceHolder1_hdnUpAdultFare").value;
    var childFareOW = GetObj("ctl00_ContentPlaceHolder1_hdnChildFare").value;
    var childFareRT = GetObj("ctl00_ContentPlaceHolder1_hdnUpChildFare").value;

    var PointUseadultFareOW = adultFareOW - fn_GetTrunc((adultFareOW * 1), 2);
    var PointUseadultFareRT = adultFareRT - fn_GetTrunc((adultFareRT * 1), 2);
    var PointUsechildFareOW = childFareOW - fn_GetTrunc((childFareOW * 1), 2);
    var PointUsechildFareRT = childFareRT - fn_GetTrunc((childFareRT * 1), 2);

    var fareOW = (adultFareOW * (adultPax + disablePax + etcPax + disableSubPax)) + (childFareOW * childPax);
    var fareRT = (adultFareRT * (adultPax + disablePax + etcPax + disableSubPax)) + (childFareRT * childPax);

    var PointUsefareOW = (PointUseadultFareOW * (adultPax + disablePax + etcPax + disableSubPax)) + (PointUsechildFareOW * childPax);
    var PointUsefareRT = (PointUseadultFareRT * (adultPax + disablePax + etcPax + disableSubPax)) + (PointUsechildFareRT * childPax);

    var pointOW = fareOW - PointUsefareOW;
    var pointRT = fareRT - PointUsefareRT;

    // 잔여포인트 >= 지불포인트 일때 Layout 표시한다.            
    if (remainPoint >= (pointOW + pointRT)) {
        //추가할인, 쿠폰 비활성화                             
        ShowDivBackgroud(); // 투명 Div 띄우기
        fn_OpenLayer("divPointUse", 500, 500);

        var lblFareOW = GetObj("ctl00_ContentPlaceHolder1_lblFareOW");    // 항공운임
        var lblPointUseOW = GetObj("ctl00_ContentPlaceHolder1_lblPointUseOW");          // 지불금액
        var lblPointOW = GetObj("ctl00_ContentPlaceHolder1_lblPointOW");      // 지불포인트                                

        var lblFareRT = GetObj("ctl00_ContentPlaceHolder1_lblFareRT");    // 항공운임
        var lblPointUseRT = GetObj("ctl00_ContentPlaceHolder1_lblPointUseRT");          // 지불금액
        var lblPointRT = GetObj("ctl00_ContentPlaceHolder1_lblPointRT");      // 지불포인트

        var lblFareAmt = GetObj("ctl00_ContentPlaceHolder1_lblFareAmt");    // 항공운임
        var lblPointUseAmt = GetObj("ctl00_ContentPlaceHolder1_lblPointUseAmt");          // 지불금액
        var lblPointAmt = GetObj("ctl00_ContentPlaceHolder1_lblPointAmt");      // 지불포인트

        var lblRemainPoint = GetObj("ctl00_ContentPlaceHolder1_lblRemainPoint");// 잔여포인트
        var lblUsePoint = GetObj("ctl00_ContentPlaceHolder1_lblUsePoint");      // 사용포인트
        var lblAfterReaminPoint = GetObj("ctl00_ContentPlaceHolder1_lblAfterReaminPoint");  //사용후잔여

        var won = "원";
        var plus = "&nbsp;&nbsp;&nbsp;+";
        var equal = "&nbsp;&nbsp;&nbsp;= ";

        var isRoundTrip = GetObj("hdnRoundTrip").value;

        if (isRoundTrip == "true") {
            lblFareOW.innerHTML = fn_InsertComma(fareOW) + won + plus;
            lblPointUseOW.innerHTML = fn_InsertComma(PointUsefareOW) + won + plus;
            lblPointOW.innerHTML = fn_InsertComma(pointOW) + won + plus;

            lblFareRT.innerHTML = fn_InsertComma(fareRT) + won + equal;
            lblPointUseRT.innerHTML = fn_InsertComma(PointUsefareRT) + won + equal;
            lblPointRT.innerHTML = fn_InsertComma(pointRT) + won + equal;
        }

        lblFareAmt.innerHTML = fn_InsertComma(fareOW + fareRT) + won;
        lblPointUseAmt.innerHTML = fn_InsertComma(PointUsefareOW + PointUsefareRT) + won;
        lblPointAmt.innerHTML = fn_InsertComma(pointOW + pointRT) + won;

        lblRemainPoint.innerHTML = fn_InsertComma(remainPoint) + won;
        lblUsePoint.innerHTML = fn_InsertComma(pointOW + pointRT) + won;
        lblAfterReaminPoint.innerHTML = fn_InsertComma(remainPoint - (pointOW + pointRT)) + won;
    }
    else {
        var msg = "잔여 수수료가 부족합니다.\n(잔여:" + fn_InsertComma(remainPoint) + "원/필요:" + fn_InsertComma(pointOW + pointRT) + "원/부족:" + fn_InsertComma(pointOW + pointRT - remainPoint) + "원)";
        fn_OpenInformation("", msg);
        GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked = false;
    }
}

function SetTotalAmt() {
    var tdTotal_Exp = GetObj("tdTotal_Exp");
    var tdTotal_Amt = GetObj("tdTotal_Amt");
    var tdTotal_Inf = GetObj("tdTotal_Inf");

    var adultPax = Number(GetObj("hdnAdult").value);
    var disablePax = Number(GetObj("hdnDisable").value);
    var disableSubPax = Number(GetObj("hdnDisableSub").value);
    var etcPax = Number(GetObj("hdnEtc").value);
    var childPax = Number(GetObj("hdnChild").value);

    var adultFareOW = Number(GetObj("ctl00_ContentPlaceHolder1_hdnAdultFare").value);
            var adultFareRT = Number(GetObj("ctl00_ContentPlaceHolder1_hdnUpAdultFare").value);
            var childFareOW = Number(GetObj("ctl00_ContentPlaceHolder1_hdnChildFare").value);
            var childFareRT = Number(GetObj("ctl00_ContentPlaceHolder1_hdnUpChildFare").value);

            var adultPointOW = 0;
            var adultPointRT = 0;
            var childPointOW = 0;
            var childPointRT = 0;

            if (GetObj("ctl00_ContentPlaceHolder1_chkPoint").checked == true) {
                adultPointOW = fn_GetTrunc((adultFareOW * 1), 2);
                adultPointRT = fn_GetTrunc((adultFareRT * 1), 2);
                childPointOW = fn_GetTrunc((childFareOW * 1), 2);
                childPointRT = fn_GetTrunc((childFareRT * 1), 2);

                var pointOW = (adultPointOW * (adultPax + disablePax + etcPax + disableSubPax)) + (childPointOW * childPax);
                var pointRT = (adultPointRT * (adultPax + disablePax + etcPax + disableSubPax)) + (childPointRT * childPax);

                GetObj("tdPoint").innerHTML = fn_InsertComma(pointOW + pointRT) + "원";
                GetObj("tbPoint").style["display"] = "";

                adultFareOW = adultFareOW - fn_GetTrunc((adultFareOW * 1), 2);
                adultFareRT = adultFareRT - fn_GetTrunc((adultFareRT * 1), 2);
                childFareOW = childFareOW - fn_GetTrunc((childFareOW * 1), 2);
                childFareRT = childFareRT - fn_GetTrunc((childFareRT * 1), 2);
            }
            else {
                GetObj("tdPoint").innerHTML = "";
                GetObj("tbPoint").style["display"] = "none";
            }

            var won = "원";
            var plus = " + ";
            var equal = " = ";
            var point = "P";
            var person = "인";

            var fareOW = (adultFareOW * (adultPax + disablePax + etcPax + disableSubPax)) + (childFareOW * childPax);
            var fareRT = (adultFareRT * (adultPax + disablePax + etcPax + disableSubPax)) + (childFareRT * childPax);

            var isRoundTrip = GetObj("hdnRoundTrip").value;

            if (isRoundTrip == "true") {
                tdTotal_Exp.innerHTML = fn_InsertComma(fareOW) + won + plus + fn_InsertComma(fareRT) + won + equal;
                tdTotal_Amt.innerHTML = fn_InsertComma(fareOW + fareRT) + won;
            }
            else {
                tdTotal_Exp.innerHTML = equal;
                tdTotal_Amt.innerHTML = fn_InsertComma(fareOW) + won;
            }

            tdTotal_Inf.innerHTML = "(";
            tdTotal_Inf.innerHTML += ((adultPax + disableSubPax + etcPax) > 0) ? "성인 " + (adultPax + disableSubPax + etcPax) + person : "";
            tdTotal_Inf.innerHTML += (childPax > 0) ? ", 소아 " + childPax + person : "";
            tdTotal_Inf.innerHTML += (disablePax > 0) ? ", 장애인 " + disablePax + person : "";
            tdTotal_Inf.innerHTML += ")";

            //최종 지불 금액
            fn_PurchaseSum();
        }

        function MoveFirstPage() {
            document.location = "RSV_ScheduleSelect.aspx";
        }

        function InputPaxName() {
            var sURL = "/RSV/RSV_InputPAXName.aspx";
            fn_OpenWindow(sURL, "InputPAXName", "870", "650", "Yes");
            return false;
        }
        //-->
        $(document).ready(function () {
            // 진마켓 이벤트 기간에 맞춰 배너 활성여부 판단 코드 추가
            var today = new Date('04-21-2017 16:59:03');          // 현재시간
            var startDateTime = new Date('08-19-2015 10:00:00');  // 이벤트 시작
            var endDateTime = new Date('08-31-2015 23:59:59');    // 이벤트 종료

            if (startDateTime.getTime() <= today.getTime() && endDateTime.getTime() >= today.getTime()) {
                $("#trEventBanner").show();

            }
            else {
                $("#trEventBanner").hide();
            }
        });

        function SetAgreement(pType) {
            GetObj("liTerm1").className = "";
            GetObj("liTerm2").className = "";
            GetObj("liTerm3").className = "";
            GetObj("liTerm4").className = "";
            GetObj("liTerm5").className = "";
            GetObj("divPersonalDataTerm1").style.display = "none";
            GetObj("divPersonalDataTerm1").className = "";
            GetObj("divPersonalDataTerm2").style.display = "none";
            GetObj("divPersonalDataTerm2").className = "";
            GetObj("divPersonalDataTerm3").style.display = "none";
            GetObj("divPersonalDataTerm3").className = "";
            GetObj("divPersonalDataTerm4").style.display = "none";
            GetObj("divPersonalDataTerm4").className = "";
            GetObj("divPersonalDataTerm5").style.display = "none";
            GetObj("divPersonalDataTerm5").className = "";

            GetObj("liTerm" + pType).className = "selected";
            GetObj("divPersonalDataTerm" + pType).style.display = "block";
            GetObj("divPersonalDataTerm" + pType).className = "terms";
        }

        function BanChild() {
            alert("입력하신 동반인 정보가 존재하지 않습니다.");
            return false;
        }

        function OKChild() {
            alert("입력하신 동반인 정보가 확인되었습니다.");
            return false;
        }

        function RetryChild() {
            alert("세션이 만료되었습니다. 다시 조회해 주세요.");
            document.location.href = "RSV_ScheduleSelect.aspx";
            return false;
        }

        var alertFlag;
        function ShowDelayinfo(pStd, pEtd) {
            if (alertFlag != "3") {
                var std = pStd.substring(0, 2) + ":" + pStd.substring(2);
                var etd = pEtd.substring(0, 2) + ":" + pEtd.substring(2);
                alert("선택하신 항공편은 " + std + " -> " + etd + " 으로 지연 출발 예정입니다.\r확인 후 예약해 주시기 바랍니다.");
            }
            return;
        }
    </script>
    <div id="divSeatCnt" style="position: absolute; width: 110px; height: 20px; z-index: 1; display: none; top: 2070px; left: 516px;">
        <table width="110" height="20" border="0" cellpadding="0" cellspacing="0">
            <tbody><tr>
                <td height="20" align="center" background="/images/ScreenTip2.gif" class="Rspink">
                    <div id="divCnt" name="divCnt">9석 / 기종:B738</div>
                </td>
            </tr>
        </tbody></table>
    </div>
    <table width="715" border="0" cellpadding="0" cellspacing="0">
        <tbody><tr>
            <td>
                <img src="/images/body_line01.gif" alt="" width="715" height="5"></td>
        </tr>
        <tr>
            <td>
                <table width="715" border="0" cellpadding="0" cellspacing="0">
                    <tbody><tr>
                        <td style="width: 15px; height: 30px"></td>
                        <td valign="bottom" style="width: 1px; padding-bottom: 2px;">
                            <h3>
                                <img src="/images/RSV_tit08.gif" alt="항공편 및 운임선택"></h3>
                        </td>
                        <td align="right" valign="bottom" class="location" style="padding-right: 5px;">홈 &gt; 항공편 예매 &gt; 국내선 예매 &gt; <strong>항공편 및 운임선택</strong>
                        </td>
                    </tr>
                </tbody></table>
                <table width="715" border="0" cellpadding="0" cellspacing="0">
                    <tbody><tr>
                        <td style="width: 15px; height: 28px;"></td>
                        <td align="right">
                            <img src="/images/Body_tit_copy.gif" alt=""></td>
                    </tr>
                </tbody></table>
            </td>
        </tr>
        <tr>
            <td align="center">
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td align="center" style="height: 19px; width: 2px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td style="width: 10px;">&nbsp;</td>
                        <td class="tit">소아 가격은 성인 가격에서 5,000원 할인됩니다.</td>
                    </tr>
                    <tr>
                        <td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td>&nbsp;</td>
                        <td class="tit">해당 항공편 출발 1시간 전까지 예매를 하실 수 있습니다.</td>
                    </tr>
                    <tr>
                        <td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td>&nbsp;</td>
                        <td class="tit">잔여 좌석이 없는 경우 "매진"으로 표시 됩니다.</td>
                    </tr>
                    <tr>
                        <td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td>&nbsp;</td>
                        <td class="tit">
                            <font color="red">성인 동반없이 소아 단독 탑승은 불가합니다.</font></td>
                    </tr>
                    <tr>
                        <td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td>&nbsp;</td>
                        <td class="tit">
                            <font color="red">할인운임은 신분, 규정 및 좌석상의 제한이 없으므로 잔여좌석이 있을 경우, 할인운임으로 구매하시기 바랍니다.</font></td>
                    </tr>
                    <tr>
                        <td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td>&nbsp;</td>
                        <td class="tit">
                            <font color="red">당일 항공편 예매 시, 운임을 클릭하여 출발 지연 여부를 확인하시기 바랍니다.</font></td>
                    </tr>
                    <tr>
                        <td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
                        <td>&nbsp;</td>
                        <td class="tit">
                            <font color="red">출발 당일, 항공기 출발 20분 전까지 공항 카운터에서 탑승수속을 진행해주시기 바랍니다.</font></td>
                    </tr>

                    <tr id="ctl00_ContentPlaceHolder1_trGroupComment" style="display: none;">
	<td align="center" style="height: 19px;">
                            <img src="/images/Body_tit_dot.gif" width="2" height="2" alt=""></td>
	<td>&nbsp;</td>
	<td class="tit">
                            <font color="red">편도의 경우 일반운임으로 적용됩니다.</font></td>
</tr>

                    <tr>
                        <td align="right" colspan="3" style="height: 10px"></td>
                    </tr>
                </tbody></table>
            </td>
        </tr>
        <tr>
            <td height="10"></td>
        </tr>
        <tr>
            <td align="center">
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr valign="top">
                        <td style="border: 1px solid #add352;">
                            <table width="335" border="0" cellpadding="1" cellspacing="1">
                                <tbody><tr valign="middle">
                                    <td align="center" bgcolor="#FFFFFF">

                                        <table width="94%" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td align="left" height="25">&nbsp;&nbsp;<img id="ctl00_ContentPlaceHolder1_ibtnPrevDate_DownLine" alt="이전일" onclick="if(!fn_Valid_UpDown_Date('ctl00_ContentPlaceHolder1_fltlstDownLine', -1)) return false;" src="/images/RSV_formerday_icon.gif" style="border-width:0px;height:13px;width:39px;cursor: pointer;"></td>
                                                <td id="ctl00_ContentPlaceHolder1_tdDownLineDate" align="center" width="72%" class="Mblue">04월 28일 금요일</td>

                                                <td align="right">
                                                    <img id="ctl00_ContentPlaceHolder1_ibtnNextDate_DownLine" alt="다음일" onclick="if(!fn_Valid_UpDown_Date('ctl00_ContentPlaceHolder1_fltlstDownLine', 1)) return false;" src="/images/RSV_nextday_icon.gif" style="border-width:0px;height:13px;width:39px;cursor: pointer;">&nbsp;&nbsp;</td>
                                            </tr>
                                        </tbody></table>
                                        <table id="ctl00_ContentPlaceHolder1_fltlstDownLine_tblFlight" width="94%" border="0" cellpadding="0" cellspacing="0">
	<tbody><tr>
		<td>
            <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#eef9cd">
                <tbody><tr>
                    <td align="center">
                        <table width="95%" border="0" cellspacing="0" cellpadding="0">
                            <tbody><tr>
                                <td>
                                    <table width="100%" height="25" border="0" cellpadding="0" cellspacing="0">
                                        <tbody><tr>
                                            <td align="center">
                                                <img src="../images/RSV_icon02.gif" width="6" height="6" alt="">
                                                <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblDate" class="Mbook"></span>
                                                <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblFlightStage">제주→김포</span>
                                                (<span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblPortion" class="Mlist">가는편</span>)
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </td>
                            </tr>
                            <tr>
                                <td height="1" align="center">
                                    
                                            <table width="94%" border="0" cellpadding="0" cellspacing="0" summary="항공편, 출-도착시간, 일반운임, 할인운임 순으로 구성된 가는편 목록표 입니다.">
                                                <caption>가는편 목록</caption>
                                                <tbody><tr>
                                                    <th scope="col" width="59px" align="center" style="background-color:#bed618; font-weight:normal" class="Mbook">
                                                        <nobr>항공편</nobr>
                                                    </th>
                                                    <td width="1px">
                                                        <img src="../images/RSV_gr_st01.gif" width="1" height="20" alt=""></td>
                                                    <th scope="col" width="80px" align="center" style="background-color:#bed618; font-weight:normal;" class="Mbook">
                                                        <nobr>출-도착시간</nobr>
                                                    </th>
                                                    <td width="1px">
                                                        <img src="../images/RSV_gr_st01.gif" width="1" height="20" alt=""></td>
                                                    <th scope="col" width="75px" align="center" style="background-color:#bed618;  font-weight:normal;" class="Mbook">
                                                        <nobr>일반운임</nobr>
                                                    </th>
                                                    
                                                    <td width="1px">
                                                        <img src="../images/RSV_gr_st01.gif" width="1" height="20" alt=""></td>
                                                    <th scope="col" width="75px" style="background-color:#bed618;  font-weight:normal;" align="center" class="Mbook">
                                                        <nobr>할인운임</nobr>
                                                    </th>
                                                    
                                                </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0302
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    07:05-08:10
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0705', '0705' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0705', '0705' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="24,800원"> 24,800원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0304
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    08:05-09:15
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="772">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0810', '0810' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="772">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0810', '0810' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="24,800원"> 24,800원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0306
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    08:25-09:35
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="772">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0825', '0825' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="772">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0825', '0825' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="24,800원"> 24,800원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0308
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    09:10-10:20
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0910', '0910' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '0910', '0910' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="34,400원"> 34,400원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0314
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    11:50-12:55
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="772">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1150', '1150' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="772">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1150', '1150' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="46,400원"> 46,400원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0316
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    12:25-13:35
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="772">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1225', '1225' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="772">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1225', '1225' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="51,200원"> 51,200원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0318
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    13:15-14:25
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1315', '1315' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1315', '1315' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="60,800원"> 60,800원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0320
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    14:00-15:05
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1400', '1400' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0324
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    15:25-16:35
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1525', '1525' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('0', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:none;" disabled="" title="80,000원"><font class="Mbook" style="font-size: 11px; letter-spacing: -1px;">매진</font> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0326
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    15:30-16:40
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1530', '1530' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('0', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:none;" disabled="" title="80,000원"><font class="Mbook" style="font-size: 11px; letter-spacing: -1px;">매진</font> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0328
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    16:25-17:35
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="772">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1625', '1625' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('0', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:none;" disabled="" title="80,000원"><font class="Mbook" style="font-size: 11px; letter-spacing: -1px;">매진</font> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="772">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0330
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    16:50-18:00
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1650', '1650' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('-133', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:none;" disabled="" title="80,000원"><font class="Mbook" style="font-size: 11px; letter-spacing: -1px;">매진</font> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0332
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    17:40-18:50
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1740', '1740' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('-133', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:none;" disabled="" title="80,000원"><font class="Mbook" style="font-size: 11px; letter-spacing: -1px;">매진</font> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0336
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    19:30-20:40
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '1930', '1930' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('0', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:none;" disabled="" title="80,000원"><font class="Mbook" style="font-size: 11px; letter-spacing: -1px;">매진</font> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0338
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    20:40-21:50
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="772">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '2040', '2040' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="772">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '2040', '2040' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 772, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="76,000원"> 76,000원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0340
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    21:05-22:15
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '2105', '2105' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '2105', '2105' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="76,000원"> 76,000원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                        
                                            <tr>
                                                <td height="22" class="Rgrcenter">
                                                    LJ0334
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter">
                                                    21:10-22:20
                                                </td>
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnREV_CLS" type="hidden" value="0">
                                                    <input name="hdnRULE" type="hidden" value="0">
                                                    <input name="hdnREMARK" type="hidden" value="FO">
                                                    <input name="hdnACTYPE" type="hidden" value="738">
                                                    
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '2110', '2110' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="Y" style="height:13px; display:inline;" title="80,000원"> 80,000원
										</label>
                                                </td>
                                                
                                                <td></td>
                                                <td class="Rgrcenter" style="text-align: right; padding-right: 4px;">
                                                    <input name="hdnE_REV_CLS" type="hidden" value="0">
                                                    <input name="hdnE_RULE" type="hidden" value="0">
                                                    <input name="hdnE_REMARK" type="hidden" value="FO">
                                                    <input name="hdnE_ACTYPE" type="hidden" value="738">
                                                    <label onclick="fn_Radio_Click(event, 'ctl00_ContentPlaceHolder1_fltlstDownLine', ' ', '2110', '2110' ); " style="cursor:pointer; vertical-align:middle;" onmouseover="fn_SeatCntView('9', 738, event);" onmouseout="fn_SeatCntHide(event);">
											<input name="rdoctl00_ContentPlaceHolder1_fltlstDownLine" type="radio" value="E" style="height:13px; display:inline;" title="76,000원"> 76,000원
										</label>
                                                </td>
                                                
                                            </tr>
                                        
                                            <tr>
                                                <td colspan="7" align="center">
                                                    <img src="../images/RSV_Grlist_line02.gif" width="292" height="1" alt=""></td>
                                            </tr>
                                            <tr id="trTemp" style="height: 10px;">
                                                <td colspan="7"></td>
                                            </tr>
                                            </tbody></table>
                                        
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
        </td>
	</tr>
	<tr>
		<td height="5"></td>
	</tr>
	<tr>
		<td>
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
                <tbody><tr>
                    <td width="21" align="center">
                        <img src="../images/RSV_icon02.gif" width="6" height="6" alt=""></td>
                    <td width="280">
                        <p class="Mpurple">
                            <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblFLT_NUM" class="Mpurple"></span>
                            <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblFLT_Discussion" class="Mpurple"></span>
                        </p>
                    </td>
                </tr>
            </tbody></table>
        </td>
	</tr>
	<tr>
		<td height="5"></td>
	</tr>
	<tr>
		<td>
            <table border="0" cellpadding="0" cellspacing="0" summary="예약변경, 환불위약금으로 구성된 가는편 운임규정 표입니다">
                <caption>가는편 운임규정</caption>
                <tbody><tr>
                    <td style="width: 4px;"></td>
                    <td width="13" align="center">
                        <img src="../images/RSV_icon03.gif" width="4" height="4" alt=""></td>
                    <th scope="row" width="60" class="Mbook" style="font-weight:normal; text-align:left;">예약변경</th>
                    <td width="283">
                        <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblREV_CLS" class="1point"></span></td>
                </tr>
                <tr>
                    <td style="width: 4px;"></td>
                    <td width="13" align="center"></td>
                    <td width="60" class="Mbook"></td>
                    <td width="283">
                        <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_Label1" class="1point">&nbsp;출발지/목적지 변경은 불가능 합니다.</span></td>
                </tr>
                <tr>
                    <td colspan="4" align="center" style="padding-top: 3px; padding-bottom: 3px;">
                        <img src="../images/agent_list_line03.gif" width="292" height="1" alt=""></td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td align="center" valign="top" style="padding-top: 6px;">
                        <img src="../images/RSV_icon03.gif" width="4" height="4" alt=""></td>
                    <th scope="row" class="Mbook" valign="top" style="font-weight:normal; text-align:left;">환불<br>위약금</th>
                    <td>
                        <span id="ctl00_ContentPlaceHolder1_fltlstDownLine_lblRULE" class="1point"></span></td>
                </tr>
                <tr>
                    <td colspan="4" align="center" style="padding-top: 3px;">
                        <img src="../images/agent_list_line03.gif" width="292" height="1" alt=""></td>
                </tr>
                
            </tbody></table>
        </td>
	</tr>
	<tr>
		<td height="10"></td>
	</tr>
</tbody></table>

<img src="/images/Jinair_ci_img.gif" id="ctl00_ContentPlaceHolder1_fltlstDownLine_imgTemp" alt="JINAIR 로고" style="vertical-align:middle;margin-bottom:25;display:none;">
<input type="submit" name="ctl00$ContentPlaceHolder1$fltlstDownLine$btnDataBind" value="" id="ctl00_ContentPlaceHolder1_fltlstDownLine_btnDataBind" style="display:none">
<input name="ctl00$ContentPlaceHolder1$fltlstDownLine$btnInitialized" type="button" id="ctl00_ContentPlaceHolder1_fltlstDownLine_btnInitialized" value="button" style="display:none" onclick="fn_GetFare('ctl00_ContentPlaceHolder1_fltlstDownLine', event);">


<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnVisible" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnVisible" value="true">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnDate" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnDate" value="20170428">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnPortion" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnPortion" value="가는편">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnDepartureAirport" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnDepartureAirport" value="제주">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnDeparture" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnDeparture" value="CJU">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnArrivalAirport" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnArrivalAirport" value="김포">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnArrival" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnArrival" value="GMP">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnRoundTrip" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnRoundTrip" value="False">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnRequestSeatCount" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnRequestSeatCount" value="1">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnGroupYN" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnGroupYN" value="N">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnFare" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnFare">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnBookingClass" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnBookingClass" value="Y">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnFLT_NUM" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnFLT_NUM">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnRule" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnRule">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnFormerFareYN" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnFormerFareYN" value="N">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnDEPT_ARRT" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnDEPT_ARRT">
<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnRowCount" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnRowCount" value="17">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hidDCSChangeYN" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hidDCSChangeYN">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnPnrSeg" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnPnrSeg">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstDownLine$hdnIsAcType" id="ctl00_ContentPlaceHolder1_fltlstDownLine_hdnIsAcType" value="Y">

                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                        <td width="10">&nbsp;</td>
                        <td style="border: 1px solid #add352;">
                            <table width="335" border="0" cellpadding="1" cellspacing="1">
                                <tbody><tr valign="middle">
                                    <td align="center" bgcolor="#FFFFFF">

                                        <table width="94%" border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td align="left" height="25">&nbsp;&nbsp;</td>
                                                <td id="ctl00_ContentPlaceHolder1_tdUpLineDate" align="center" class="Mblue">&nbsp;</td>

                                                <td align="right">
                                                    &nbsp;&nbsp;</td>
                                            </tr>
                                        </tbody></table>
                                        <table id="ctl00_ContentPlaceHolder1_fltlstUpLine_tblFlight" width="94%" border="0" cellpadding="0" cellspacing="0" style="display:none;">
	<tbody><tr>
		<td>
            <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#e8f8db">
                <tbody><tr>
                    <td align="center">
                        <table width="95%" border="0" cellspacing="0" cellpadding="0">
                            <tbody><tr>
                                <td>
                                    <table width="100%" height="25" border="0" cellpadding="0" cellspacing="0">
                                        <tbody><tr>
                                            <td align="center">
                                                <img src="../images/RSV_icon02.gif" width="6" height="6" alt="">
                                                <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblDate" class="Mbook"></span>
                                                <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblFlightStage">김포→제주</span>
                                                (<span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblPortion" class="Mlist">오는편</span>)
                                            </td>
                                        </tr>
                                    </tbody></table>
                                </td>
                            </tr>
                            <tr>
                                <td height="1" align="center">
                                    
                                </td>
                            </tr>
                        </tbody></table>
                    </td>
                </tr>
            </tbody></table>
        </td>
	</tr>
	<tr>
		<td height="5"></td>
	</tr>
	<tr>
		<td>
            <table width="100%" border="0" cellpadding="0" cellspacing="0">
                <tbody><tr>
                    <td width="21" align="center">
                        <img src="../images/RSV_icon02.gif" width="6" height="6" alt=""></td>
                    <td width="280">
                        <p class="Mpurple">
                            <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblFLT_NUM" class="Mpurple"></span>
                            <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblFLT_Discussion" class="Mpurple"></span>
                        </p>
                    </td>
                </tr>
            </tbody></table>
        </td>
	</tr>
	<tr>
		<td height="5"></td>
	</tr>
	<tr>
		<td>
            <table border="0" cellpadding="0" cellspacing="0" summary="예약변경, 환불위약금으로 구성된 가는편 운임규정 표입니다">
                <caption>가는편 운임규정</caption>
                <tbody><tr>
                    <td style="width: 4px;"></td>
                    <td width="13" align="center">
                        <img src="../images/RSV_icon03.gif" width="4" height="4" alt=""></td>
                    <th scope="row" width="60" class="Mbook" style="font-weight:normal; text-align:left;">예약변경</th>
                    <td width="283">
                        <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblREV_CLS" class="1point"></span></td>
                </tr>
                <tr>
                    <td style="width: 4px;"></td>
                    <td width="13" align="center"></td>
                    <td width="60" class="Mbook"></td>
                    <td width="283">
                        <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_Label1" class="1point">&nbsp;출발지/목적지 변경은 불가능 합니다.</span></td>
                </tr>
                <tr>
                    <td colspan="4" align="center" style="padding-top: 3px; padding-bottom: 3px;">
                        <img src="../images/agent_list_line03.gif" width="292" height="1" alt=""></td>
                </tr>
                <tr>
                    <td>&nbsp;</td>
                    <td align="center" valign="top" style="padding-top: 6px;">
                        <img src="../images/RSV_icon03.gif" width="4" height="4" alt=""></td>
                    <th scope="row" class="Mbook" valign="top" style="font-weight:normal; text-align:left;">환불<br>위약금</th>
                    <td>
                        <span id="ctl00_ContentPlaceHolder1_fltlstUpLine_lblRULE" class="1point"></span></td>
                </tr>
                <tr>
                    <td colspan="4" align="center" style="padding-top: 3px;">
                        <img src="../images/agent_list_line03.gif" width="292" height="1" alt=""></td>
                </tr>
                
            </tbody></table>
        </td>
	</tr>
	<tr>
		<td height="10"></td>
	</tr>
</tbody></table>

<img src="/images/Jinair_ci_img.gif" id="ctl00_ContentPlaceHolder1_fltlstUpLine_imgTemp" alt="JINAIR 로고" style="vertical-align: middle; margin-bottom: 25;">
<input type="submit" name="ctl00$ContentPlaceHolder1$fltlstUpLine$btnDataBind" value="" id="ctl00_ContentPlaceHolder1_fltlstUpLine_btnDataBind" style="display:none">
<input name="ctl00$ContentPlaceHolder1$fltlstUpLine$btnInitialized" type="button" id="ctl00_ContentPlaceHolder1_fltlstUpLine_btnInitialized" value="button" style="display:none">


<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnVisible" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnVisible" value="false">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnDate" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnDate" value="20170401">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnPortion" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnPortion" value="오는편">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnDepartureAirport" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnDepartureAirport" value="제주">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnDeparture" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnDeparture" value="CJU">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnArrivalAirport" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnArrivalAirport" value="김포">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnArrival" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnArrival" value="GMP">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnRoundTrip" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnRoundTrip" value="False">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnRequestSeatCount" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnRequestSeatCount" value="1">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnGroupYN" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnGroupYN" value="N">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnFare" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnFare">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnBookingClass" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnBookingClass">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnFLT_NUM" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnFLT_NUM">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnRule" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnRule">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnFormerFareYN" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnFormerFareYN" value="N">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnDEPT_ARRT" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnDEPT_ARRT">
<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnRowCount" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnRowCount" value="16">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hidDCSChangeYN" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hidDCSChangeYN">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnPnrSeg" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnPnrSeg">

<input type="hidden" name="ctl00$ContentPlaceHolder1$fltlstUpLine$hdnIsAcType" id="ctl00_ContentPlaceHolder1_fltlstUpLine_hdnIsAcType" value="Y">

                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
            </td>
        </tr>
        <tr>
            <td align="center">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnAdult" id="ctl00_ContentPlaceHolder1_hdnAdult" value="1">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnChild" id="ctl00_ContentPlaceHolder1_hdnChild" value="0">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnInfant" id="ctl00_ContentPlaceHolder1_hdnInfant" value="0">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnDisable" id="ctl00_ContentPlaceHolder1_hdnDisable" value="0">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnDisableSub" id="ctl00_ContentPlaceHolder1_hdnDisableSub" value="0">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEtc" id="ctl00_ContentPlaceHolder1_hdnEtc" value="0">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnPaxCnt" id="ctl00_ContentPlaceHolder1_hdnPaxCnt" value="1">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnTax_DownLine" id="ctl00_ContentPlaceHolder1_hdnTax_DownLine">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnTax_UpLine" id="ctl00_ContentPlaceHolder1_hdnTax_UpLine">
                
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnRoundTrip" id="ctl00_ContentPlaceHolder1_hdnRoundTrip" value="false">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnMem_FamilyName" id="ctl00_ContentPlaceHolder1_hdnMem_FamilyName">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnMem_GivenName" id="ctl00_ContentPlaceHolder1_hdnMem_GivenName">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnMem_Sex" id="ctl00_ContentPlaceHolder1_hdnMem_Sex" value="F">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnDeparture" id="ctl00_ContentPlaceHolder1_hdnDeparture" value="CJU">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnArrival" id="ctl00_ContentPlaceHolder1_hdnArrival" value="GMP">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnAuth" id="ctl00_ContentPlaceHolder1_hdnAuth">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnGroupYN" id="ctl00_ContentPlaceHolder1_hdnGroupYN" value="N">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnApprovalSeq" id="ctl00_ContentPlaceHolder1_hdnApprovalSeq">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnPNR_NO" id="ctl00_ContentPlaceHolder1_hdnPNR_NO">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnMEM_CLASS" id="ctl00_ContentPlaceHolder1_hdnMEM_CLASS" value="I">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnComplete" id="ctl00_ContentPlaceHolder1_hdnComplete">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnPurchaseSum" id="ctl00_ContentPlaceHolder1_hdnPurchaseSum">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnRSV_MBR_GB" id="ctl00_ContentPlaceHolder1_hdnRSV_MBR_GB" value="NP">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnIsFareDriven" id="ctl00_ContentPlaceHolder1_hdnIsFareDriven" value="N">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEmbargo" id="ctl00_ContentPlaceHolder1_hdnEmbargo">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnCP_ID" id="ctl00_ContentPlaceHolder1_hdnCP_ID">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnCP_USERID" id="ctl00_ContentPlaceHolder1_hdnCP_USERID">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnAdultFare" id="ctl00_ContentPlaceHolder1_hdnAdultFare">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnChildFare" id="ctl00_ContentPlaceHolder1_hdnChildFare">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnUpAdultFare" id="ctl00_ContentPlaceHolder1_hdnUpAdultFare">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnUpChildFare" id="ctl00_ContentPlaceHolder1_hdnUpChildFare">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnIsLogin" id="ctl00_ContentPlaceHolder1_hdnIsLogin" value="N">
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td style="width: 130px;" class="Mpurple">&nbsp;&nbsp;&nbsp;총 항공운임</td>
                        <td style="width: 22px;">
                            <img src="/images/RSV_gr_st03.gif" width="22" height="30" alt=""></td>
                        <td id="ctl00_ContentPlaceHolder1_tdTotal_Exp" style="width: 220px;" align="right">&nbsp;</td>

                        <td id="ctl00_ContentPlaceHolder1_tdTotal_Amt" style="width: 100px;" align="right">&nbsp;</td>

                        <td id="ctl00_ContentPlaceHolder1_tdTotal_Inf">&nbsp;</td>

                    </tr>
                    <tr>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                    </tr>
                    <tr>
                        <td class="Mpurple">&nbsp;&nbsp;&nbsp;공항사용료</td>
                        <td>
                            <img src="/images/RSV_gr_st03.gif" width="22" height="30" alt=""></td>
                        <td id="ctl00_ContentPlaceHolder1_tdTax_Exp" align="right">&nbsp;</td>

                        <td id="ctl00_ContentPlaceHolder1_tdTax_Amt" align="right">&nbsp;</td>

                        <td id="ctl00_ContentPlaceHolder1_tdTax_Inf">&nbsp;</td>

                    </tr>
                    <tr>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                        <td style="background-color: #C1D72E; height: 1px;"></td>
                    </tr>
                    <tr id="ctl00_ContentPlaceHolder1_trFuel_Line01">
	<td class="Mpurple">&nbsp;&nbsp;&nbsp;유류할증료</td>
	<td>
                            <img src="/images/RSV_gr_st03.gif" width="22" height="30" alt=""></td>
	<td id="ctl00_ContentPlaceHolder1_tdFuel_Exp" align="right">&nbsp;</td>
	<td id="ctl00_ContentPlaceHolder1_tdFuel_Amt" align="right">&nbsp;</td>
	<td id="ctl00_ContentPlaceHolder1_tdFuel_Inf">&nbsp;</td>
</tr>

                    <tr id="ctl00_ContentPlaceHolder1_trFuel_Line02">
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
</tr>

                </tbody></table>
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td>
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr id="ctl00_ContentPlaceHolder1_trADiscount_Line1">
	<td style="width: 130px;" class="Mpurple">&nbsp;&nbsp;&nbsp;추가 할인</td>
	<td style="width: 22px;">
                                        <img src="/images/RSV_gr_st03.gif" width="22" height="30" alt=""></td>
	<td id="ctl00_ContentPlaceHolder1_tdADiscount_Exp" style="width: 220px;" align="right">&nbsp;</td>
	<td id="ctl00_ContentPlaceHolder1_tdADiscount_Amt" style="width: 100px;" align="right">&nbsp;</td>
	<td id="ctl00_ContentPlaceHolder1_tdADiscount_Inf" align="left">&nbsp;</td>
</tr>

                                <tr id="ctl00_ContentPlaceHolder1_trADiscount_Line2">
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
</tr>

                            </tbody></table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr id="ctl00_ContentPlaceHolder1_trCoupon_Line1">
	<td style="width: 130px;" class="Mpurple">&nbsp;&nbsp;&nbsp;쿠폰</td>
	<td style="width: 22px;">
                                        <img src="/images/RSV_gr_st03.gif" width="22" height="30" alt=""></td>
	<td style="width: 220px;" align="right">&nbsp;=</td>
	<td id="ctl00_ContentPlaceHolder1_tdCoupon_Amt" style="width: 100px;" align="right">&nbsp;</td>
	<td>&nbsp;</td>
</tr>

                                <tr id="ctl00_ContentPlaceHolder1_trCoupon_Line2">
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
	<td style="background-color: #C1D72E; height: 1px;"></td>
</tr>

                            </tbody></table>
                        </td>
                    </tr>
                    <tr>
                        <td style="height: 10;"></td>
                    </tr>
                </tbody></table>
                
                <table id="tbPoint" width="685" border="0" cellspacing="0" cellpadding="0" style="display: none">
                    <tbody><tr>
                        <td style="width: 130px;" height="24" bgcolor="#ddeeab" class="Mpurple">&nbsp;&nbsp;&nbsp;지불 금액</td>
                        <td style="width: 22px;" bgcolor="#ddeeab">
                            <img src="/images/RSV_Grlist_st03.gif" width="15" height="24" alt=""></td>
                        <td style="width: 200px;" bgcolor="#ddeeab">&nbsp;</td>
                        <td id="ctl00_ContentPlaceHolder1_tdPurchase" style="width: 120px;" align="right" bgcolor="#ddeeab" class="Mpink">&nbsp;</td>

                        <td bgcolor="#ddeeab">&nbsp;</td>
                    </tr>
                    <tr>
                        <td colspan="5" style="height: 1;"></td>
                    </tr>
                    <tr>
                        <td style="width: 130px;" height="24" bgcolor="#ddeeab" class="Mpurple">&nbsp;&nbsp;&nbsp;수수료</td>
                        <td style="width: 22px;" bgcolor="#ddeeab">
                            <img src="/images/RSV_Grlist_st03.gif" width="15" height="24" alt=""></td>
                        <td style="width: 200px;" bgcolor="#ddeeab">&nbsp;</td>
                        <td id="ctl00_ContentPlaceHolder1_tdPoint" style="width: 120px;" align="right" bgcolor="#ddeeab">&nbsp;</td>

                        <td bgcolor="#ddeeab">&nbsp;</td>
                    </tr>
                    <tr>
                        <td colspan="5" style="height: 1;"></td>
                    </tr>
                </tbody></table>
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td style="width: 130px;" height="24" bgcolor="#ddeeab" class="Mpurple">&nbsp;&nbsp;&nbsp;총 금액</td>
                        <td style="width: 22px;" bgcolor="#ddeeab">
                            <img src="/images/RSV_Grlist_st03.gif" width="15" height="24" alt=""></td>
                        <td style="width: 200px;" bgcolor="#ddeeab">&nbsp;</td>
                        <td id="ctl00_ContentPlaceHolder1_tdTotal" style="width: 120px;" align="right" bgcolor="#ddeeab">&nbsp;</td>

                        <td bgcolor="#ddeeab">&nbsp;</td>
                    </tr>
                    <tr>
                        <td colspan="5" style="height: 10;"></td>
                    </tr>
                </tbody></table>
            </td>
        </tr>
        
        <tr id="ctl00_ContentPlaceHolder1_trLogin">
	<td align="center">
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td align="right">
                            <input type="image" name="ctl00$ContentPlaceHolder1$btnPrev" id="ctl00_ContentPlaceHolder1_btnPrev" src="/images/RSV_pre_btn.gif" alt="이전" onclick="return fn_GoScheduleSelect();" style="border-width:0px;">
                            <input type="image" name="ctl00$ContentPlaceHolder1$ibtnLogin" id="ctl00_ContentPlaceHolder1_ibtnLogin" src="../images/RSV_daum_btn.gif" alt="다음" onclick="if(!fn_Validation_Login()) return false;" style="border-width:0px;">
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr id="ctl00_ContentPlaceHolder1_trCoupon" style="display:none;">
	<td align="center" style="padding-bottom: 5px;">
                <table width="685px" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td style="height: 25px; width: 141px;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;쿠폰
                        </td>
                        <td style="width: 544px; text-align: left;" background="/images/RSV_Grlist_line05.gif">&nbsp;
                            <select name="ctl00$ContentPlaceHolder1$ddlCoupon" id="ctl00_ContentPlaceHolder1_ddlCoupon" onchange="fn_ddlCoupon_Change(event);" style="color:#666666;font-size:9pt;">

	</select>
                            <span id="ctl00_ContentPlaceHolder1_lblCouponText"></span>
                        </td>
                    </tr>
                    <tr id="trCouponComment1">
                        <td colspan="2" style="padding-top: 5px; width: 685px; height: 20px;">&nbsp;<img src="/images/RSV_copy_icon.gif" width="10px" height="10" alt="">
                            쿠폰을 선택하시면 포인트만큼 할인된 금액으로 결제됩니다.
                        </td>
                    </tr>
                </tbody></table>
                <table width="685px" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr id="trCouponComment2" style="display: none">
                        <td style="width: 685px; height: 20px;">&nbsp;<img src="/images/RSV_copy_icon.gif" width="10px" height="10px" alt="">
                            한번 사용한 쿠폰은 예약 변경 및 환불시 소멸되므로 재사용이 불가합니다.
                        </td>
                    </tr>
                    <tr id="trCouponComment3" style="display: none">
                        <td style="width: 685px; height: 20px;">&nbsp;<img src="/images/RSV_copy_icon.gif" width="10px" height="10px" alt="">
                            
                            쿠폰은 예매시 편도로 1매만 사용하실 수 있습니다.
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>


        <tr id="ctl00_ContentPlaceHolder1_trADiscount" style="display:none;">
	<td align="center" width="715px;">
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td width="27%" height="21" valign="bottom" style="padding-bottom: 5px;">
                            <img src="/images/RSV_Pdetail_eventdc.gif" alt="추가 할인">
                        </td>
                    </tr>
                    <tr>
                        <td style="height: 28;">
                            <table width="100%" border="0" cellspacing="0" cellpadding="0" summary="추가 할인 선택 표입니다">
                                <caption>추가 할인 선택</caption>
                                <tbody><tr>
                                    <th scope="row" style="height: 25px; width: 141px; text-align: left;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                                        <label for="ctl00_ContentPlaceHolder1_ddlADiscount" id="ctl00_ContentPlaceHolder1_Label2">추가 할인 선택</label>
                                    </th>
                                    <td style="text-align: left;" colspan="3" background="/images/RSV_Grlist_line05.gif" class="Mpink">
                                        <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                            <tbody><tr>
                                                <td style="width: 180px;">&nbsp;
                                                    <select name="ctl00$ContentPlaceHolder1$ddlADiscount" id="ctl00_ContentPlaceHolder1_ddlADiscount" onchange="fn_ddlADiscount_Change(event);" style="color:#666666;font-size:9pt;width:150px;">
		<option value="">선택</option>

	</select>
                                                </td>
                                                <td>
                                                    <input id="ctl00_ContentPlaceHolder1_rdoADiscountIsUse01" type="radio" name="ctl00$ContentPlaceHolder1$ADiscountIsUse" value="rdoADiscountIsUse01" onclick="fn_ddlADiscount_Change(event);"><label for="ctl00_ContentPlaceHolder1_rdoADiscountIsUse01">적용</label>
                                                    <input id="ctl00_ContentPlaceHolder1_rdoADiscountIsUse02" type="radio" name="ctl00$ContentPlaceHolder1$ADiscountIsUse" value="rdoADiscountIsUse02" checked="checked" onclick="fn_ddlADiscount_Change(event);"><label for="ctl00_ContentPlaceHolder1_rdoADiscountIsUse02">비적용</label>
                                                </td>
                                            </tr>
                                        </tbody></table>
                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <table width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr id="trADiscountComment01" style="display: none;">
                                    <td style="width: 5px; height: 25px; padding-left: 5px; padding-top: 3px;" valign="top">
                                        <img src="/images/RSV_copy_icon.gif" width="10" height="10" alt="">
                                    </td>
                                    <td style="padding-left: 5px;">
                                        <span id="ctl00_ContentPlaceHolder1_lblADiscountComment01"></span>
                                    </td>
                                </tr>
                                <tr id="trADiscountComment02" style="display: none;">
                                    <td style="width: 5px; height: 25px; padding-left: 5px; padding-top: 3px;" valign="top">
                                        <img src="/images/RSV_copy_icon.gif" width="10" height="10" alt="">
                                    </td>
                                    <td style="padding-left: 5px;">
                                        <span id="ctl00_ContentPlaceHolder1_lblADiscountComment02"></span>
                                    </td>
                                </tr>
                                <tr id="trADiscountComment03" style="display: none;">
                                    <td style="width: 5px; height: 25px; padding-left: 5px; padding-top: 3px;" valign="top">
                                        <img src="/images/RSV_copy_icon.gif" width="10" height="10" alt="">
                                    </td>
                                    <td style="padding-left: 5px;">
                                        <span id="ctl00_ContentPlaceHolder1_lblADiscountComment03">본인 및 배우자의 직계존비속 가족이란?<br>
                                            - 본인 및 배우자의 부모, 조부모, 외조부모, 자녀, 손자, 손녀(장인, 장모, 시부모 포함)가 할인 대상입니다.<br>
                                            - 형제, 자매는 방계 가족으로 할인 대상에서 제외됩니다.<br>
                                            - 단, 항공권 운임을 내지 않는 유아(생후 24개월 미만)의 경우 할인대상에서 제외됩니다.</span>
                                    </td>
                                </tr>
                                <tr id="trADiscountComment04" style="display: none;">
                                    <td style="width: 5px; height: 25px; padding-left: 5px; padding-top: 3px;" valign="top">
                                        <img src="/images/RSV_copy_icon.gif" width="10" height="10" alt="">
                                    </td>
                                    <td style="padding-left: 5px;">
                                        <span id="ctl00_ContentPlaceHolder1_lblADiscountComment04"></span>
                                    </td>
                                </tr>
                                <tr id="trADiscountComment05" style="display: none;">
                                    <td style="width: 5px; height: 25px; padding-left: 5px; padding-top: 3px;" valign="top">
                                        <img src="/images/RSV_copy_icon.gif" width="10" height="10" alt="">
                                    </td>
                                    <td style="padding-left: 5px;">
                                        <span id="ctl00_ContentPlaceHolder1_lblADiscountComment05">제주도민 또는 재외도민/명예도민 적용 대상 여부를 반드시 확인하시기 바랍니다. 재외도민/명예도민은 주말이나 성수기에는 할인되지 않습니다.</span>
                                    </td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <input id="ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree" type="checkbox" name="ctl00$ContentPlaceHolder1$chkCompanyDiscountAgree"><label for="ctl00_ContentPlaceHolder1_chkCompanyDiscountAgree">상단의 기업 우대 할인 이용 규정을 확인하였으며 이용 규정에 동의합니다.</label>
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr id="ctl00_ContentPlaceHolder1_trOnlyChild" align="center" style="display: none;">
	<td>
                <table width="685" border="0" cellpadding="0" cellspacing="0">
                    <tbody><tr>
                        <td colspan="3" style="height:10px;"></td>
                    </tr>
                    <tr>
                        <td colspan="3" width="27%" height="21" valign="centor">
                            <img src="/images/RSV_Pdetail_tit14.gif" width="113" height="14" alt=""></td>
                    </tr>
                    <tr>
                        <td colspan="3">
                            <table width="100%" style="height: 30;" border="0" cellpadding="0" cellspacing="0">
                                <tbody><tr>
                                    <td style="width: 3%; height: 27;">&nbsp;<img src="/images/RSV_copy_icon.gif" width="10" height="10" alt=""></td>
                                    <td style="width: 97%;">탑승자 정보 입력전, 소아와 함께 여행할 성인 승객의 예약 정보를 아래에 입력하여 소아와 성인 여정의 일치 여부를 확인해 주시기 바랍니다. (*예약 시, 기재한 정보 기준)</td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                    <tr>
                        <td style="height: 25; width: 35%;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                        <label for="ctl00_ContentPlaceHolder1_txtParentsPnr" id="ctl00_ContentPlaceHolder1_Label12">예약번호</label>
                        </td>
                        <td style="height: 25; width: 35%;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                        <label for="ctl00_ContentPlaceHolder1_txtParentsName" id="ctl00_ContentPlaceHolder1_Label10">성명</label>
                        </td>
                                                <td style="height: 25;" background="/images/RSV_Grlist_line04.gif" class="Mpurple"></td>
                    </tr>
                    <tr>
                        <td style="text-align: left;" class="Mpink">&nbsp;<input name="ctl00$ContentPlaceHolder1$txtParentsPnr" type="text" maxlength="9" id="ctl00_ContentPlaceHolder1_txtParentsPnr" class="input_01" style="width:150px;"></td>
                        <td style="text-align: left;" class="Mpink">&nbsp;<input name="ctl00$ContentPlaceHolder1$txtParentsName" type="text" maxlength="30" id="ctl00_ContentPlaceHolder1_txtParentsName" class="input_01" style="width:150px;"></td>
                        <td>&nbsp;&nbsp;<input type="image" name="ctl00$ContentPlaceHolder1$btnParentsChk" id="ctl00_ContentPlaceHolder1_btnParentsChk" src="/images/RSV_02/btn_confirm.jpg" style="border-width:0px;"></td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr>
            <td align="center">
                
            </td>
        </tr>
        <tr>
            <td>&nbsp;</td>
        </tr>
        <tr id="ctl00_ContentPlaceHolder1_trCustomer_Info" align="center" style="display:none;">
	<td>
                <table width="685" border="0" cellpadding="0" cellspacing="0">
                    <tbody><tr id="ctl00_ContentPlaceHolder1_trInputPax">
		<td style="height: 25; width: 141;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;이름 입력</td>
		<td style="width: 544; text-align: left; padding-left: 4px" colspan="3" background="/images/RSV_Grlist_line05.gif" class="Mpink">
                            <input type="image" name="ctl00$ContentPlaceHolder1$ibtnInputPaxName" id="ctl00_ContentPlaceHolder1_ibtnInputPaxName" src="/images/RSV_nameinput_btn.gif" alt="이름입력" onclick="return InputPaxName();" style="border-width:0px;"></td>
	</tr>
	
                    <tr id="ctl00_ContentPlaceHolder1_trGroupGubun">
		<td style="height: 25; width: 141;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;그룹 수요 성격</td>
		<td style="width: 544; text-align: left;" colspan="3" background="/images/RSV_Grlist_line05.gif" class="Mpink">
                            <table border="0" cellpadding="0" cellspacing="0">
                                <tbody><tr>
                                    <td>&nbsp;<select name="ctl00$ContentPlaceHolder1$ddlGroup_Gubun" id="ctl00_ContentPlaceHolder1_ddlGroup_Gubun" title="그룹 수요 성격" onchange="fn_ddlGroup_Gubun_Change();" style="color:#666666;font-size:9pt;">
			<option value="ST">학생 단체</option>
			<option value="GF">GOLF 단체</option>
			<option value="PK">패키지</option>
			<option value="IN">인센티브</option>
			<option value="IB">인바운드 단체</option>
			<option value="RG">종교 단체</option>
			<option value="SM">세미나 단체</option>
			<option value="BC">방송 단체</option>
			<option value="ET">기타 단체</option>

		</select>&nbsp;</td>
                                    <td>
                                        <select name="ctl00$ContentPlaceHolder1$ddlNation" id="ctl00_ContentPlaceHolder1_ddlNation" title="국가" style="color:#666666;font-size:9pt;">
			<option value=""></option>
			<option value="JPN">일본</option>
			<option value="CHN">중국</option>
			<option value="SEA">동남아</option>
			<option value="ETC">기타</option>

		</select></td>
                                    <td>&nbsp;
                                        <input name="ctl00$ContentPlaceHolder1$txtGroup_Etc" type="text" maxlength="50" id="ctl00_ContentPlaceHolder1_txtGroup_Etc" class="input_01" title="그룹 이름"></td>
                                </tr>
                            </tbody></table>
                        </td>
	</tr>
	
                    <tr>
                        <td style="height: 25; width: 20%;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                        <label for="ctl00_ContentPlaceHolder1_txtMobile" id="ctl00_ContentPlaceHolder1_Label3">휴대폰</label>
                        </td>
                        <td style="width: 30%; text-align: left;" background="/images/RSV_Grlist_line05.gif" class="Mpink">&nbsp;<input name="ctl00$ContentPlaceHolder1$txtMobile" type="text" maxlength="20" id="ctl00_ContentPlaceHolder1_txtMobile" class="input_01" style="width:150px;width:95%;"></td>
                        <td style="height: 25; width: 20%;" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                        <label for="ctl00_ContentPlaceHolder1_txtEmail" id="ctl00_ContentPlaceHolder1_Label4">이메일</label>
                        </td>
                        <td style="width: 30%; text-align: left;" background="/images/RSV_Grlist_line05.gif" class="Mpink">&nbsp;<input name="ctl00$ContentPlaceHolder1$txtEmail" type="text" maxlength="255" id="ctl00_ContentPlaceHolder1_txtEmail" class="input_01" style="width:150px;width:95%;"></td>
                    </tr>
                    <tr>
                        <td colspan="4">
                            <table width="100%" style="height: 30;" border="0" cellpadding="0" cellspacing="0">
                                <tbody><tr>
                                    <td style="width: 3%; height: 27;">&nbsp;<img src="/images/RSV_copy_icon.gif" width="10" height="10" alt=""></td>
                                    <td style="width: 97%;">입력하신 휴대폰으로 운항편 비정상상황시 SMS발송되며 이메일로는 구매확인증이 송부됩니다.</td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr id="ctl00_ContentPlaceHolder1_trPayment1" align="center" style="display:none;">
	<td>
                <table width="685" border="0" cellspacing="0" cellpadding="0">
                    <tbody><tr>
                        <td height="30">
                            <img src="/images/RSV_Pdetail_tit04.gif" alt="결제 방식"></td>
                    </tr>
                    <tr>
                        <td>
                            <table width="685" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr>
                                    <td style="background: #e2f2ad; border-top: solid 1px #cbe39d; border-bottom: solid 1px #cbe39d; height: 34px; vertical-align: middle; padding-left: 20px;">
                                        <table width="665" border="0" cellspacing="0" cellpadding="0">
                                            <tbody><tr>
                                                <td>
                                                    <input id="ctl00_ContentPlaceHolder1_rdoCard" type="radio" name="ctl00$ContentPlaceHolder1$Apply" value="rdoCard" checked="checked" onclick="javascript:SetAccountType();"><label for="ctl00_ContentPlaceHolder1_rdoCard">카드결제</label>
                                                    
                                                    <input id="ctl00_ContentPlaceHolder1_rdoBank" type="radio" name="ctl00$ContentPlaceHolder1$Apply" value="rdoBank" onclick="javascript:SetAccountType();"><label for="ctl00_ContentPlaceHolder1_rdoBank">실시간 계좌이체</label>
                                                    <span title="카카오페이"><input id="ctl00_ContentPlaceHolder1_rdoKKAO" type="radio" name="ctl00$ContentPlaceHolder1$Apply" value="rdoKKAO" onclick="javascript:SetAccountType();"></span><img src="/images/btn_s.png" style="vertical-align: middle" alt="카카오페이">
                                                    
                                                    
                                                </td>
                                            </tr>
                                        </tbody></table>
                                    </td>
                                </tr>
                                <tr>
                                    <td height="10"></td>
                                </tr>
                                <tr>
                                    <td height="10"></td>
                                </tr>
                            </tbody></table>
                            <table id="tbCard" style="display: none;" width="685" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr>
                                    <td colspan="4" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr height="25">
                                    <th id="cardType_label" height="25" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                                        <label for="ctl00_ContentPlaceHolder1_ddl_card_cd" id="ctl00_ContentPlaceHolder1_Label5">카드종류</label>
                                    </th>
                                    <td headers="cardType_label" background="/images/RSV_Grlist_line06.gif">&nbsp;
                                        <select name="ctl00$ContentPlaceHolder1$ddl_card_cd" id="ctl00_ContentPlaceHolder1_ddl_card_cd" class="input_F" style="width: 110px;">
		<option selected="selected" value="">카드선택</option>
		<option value="047">롯데카드</option>
		<option value="031">삼성카드</option>
		<option value="027">현대카드</option>
		<option value="026">비씨카드</option>
		<option value="029">신한카드</option>
		<option value="016">국민카드</option>
		<option value="008">하나(외환)</option>
		<option value="018">NH농협</option>
		<option value="006">하나카드</option>
		<option value="022">씨티카드</option>
		<option value="021">우리카드</option>
		<option value="002">광주은행</option>
		<option value="010">전북은행</option>
		<option value="011">제주은행</option>
		<option value="017">수협</option>
		<option value="058">산업은행</option>

	</select>
                                    </td>
                                    <td id="inllMonth_label" height="25" background="/images/RSV_Grlist_line04.gif" class="Mpurple">&nbsp;&nbsp;&nbsp;
                                        <label for="ctl00_ContentPlaceHolder1_ddl_install_period" id="ctl00_ContentPlaceHolder1_Label6">할부개월</label>
                                    </td>
                                    <td headers="inllMonth_label" background="/images/RSV_Grlist_line06.gif">&nbsp;
                                        <select name="ctl00$ContentPlaceHolder1$ddl_install_period" id="ctl00_ContentPlaceHolder1_ddl_install_period" class="input_F" style="width: 110px;">
		<option selected="selected" value="00">일시불</option>
		<option value="02">2개월</option>
		<option value="03">3개월</option>
		<option value="04">4개월</option>
		<option value="05">5개월</option>
		<option value="06">6개월</option>
		<option value="07">7개월</option>
		<option value="08">8개월</option>
		<option value="09">9개월</option>
		<option value="10">10개월</option>
		<option value="11">11개월</option>
		<option value="12">12개월</option>

	</select>
                                    </td>
                                </tr>

                                <tr>
                                    <td colspan="4" style="padding: 12px 0px 12px 20px;">
                                        <table border="0" cellpadding="0" cellspacing="0" width="100%">
                                            <tbody><tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td colspan="3" style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">안전한 신용거래를 위해 <span class="tit">안전결제(ISP)</span> 혹은 <span class="tit">안심클릭(MPI)</span>
                                                    인증이 가능한 국내발행 카드에 한해 결제하실 수 있습니다.</td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td colspan="3" style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">결제금액이 <span class="tit">30만원이 넘는 경우 공인인증서</span> 사용이 의무화되어 있습니다.</td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td colspan="3" style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">카드사 별 결제모듈이 제대로 설치가 되지 않은 경우에는 결제가 정상적으로 진행되지 않습니다.
                                                    
                                                </td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td colspan="3" style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">
                                                    <span class="tit">해외발행 카드 사용의 경우 진에어 해외사이트</span>에서 결제하실 수 있습니다.</td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">
                                                    <span class="tit">일부 선불카드(기프트카드)</span>는 사용하실 수 없습니다.  
                                                </td>
                                                <td style="text-align: right">
                                                    <input type="image" name="ctl00$ContentPlaceHolder1$btnPUCard" id="ctl00_ContentPlaceHolder1_btnPUCard" src="/images/popup/btn_card_info.gif" alt="무이자 할부 및 혜택 안내 (새창열림)" align="absmiddle" onclick="fn_OpenModaless('/RSV/PUCard_Info.html','cinfo','496','650','no'); return false;" style="border-width:0px;cursor:pointer;">
                                                </td>
                                            </tr>
                                        </tbody></table>
                                    </td>
                                </tr>
                                <tr>
                                    <td colspan="4" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                            </tbody></table>
                            <table id="tbPrivateCard" style="display: none;" width="100%" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr>
                                    <td colspan="3" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td width="20%" height="30" class="Mpurple" style="padding-left: 20px">카드번호</td>
                                    <td width="42%">
                                        <input name="ctl00$ContentPlaceHolder1$txtCardNo01" type="text" maxlength="4" id="ctl00_ContentPlaceHolder1_txtCardNo01" class="input_01" title="카드번호 앞자리" onkeypress="fn_CheckNumberTextBox(event);" onkeyup="fn_NextFocus('txtCardNo01', 'txtCardNo02', 4)" style="width:50px;text-align:right;">
                                        <input name="ctl00$ContentPlaceHolder1$txtCardNo02" type="password" maxlength="4" id="ctl00_ContentPlaceHolder1_txtCardNo02" class="input_01" title="카드번호 두번째자리" onkeypress="fn_CheckNumberTextBox(event);" onkeyup="fn_NextFocus('txtCardNo02', 'txtCardNo03', 4)" style="width:50px;text-align:right;">
                                        <input name="ctl00$ContentPlaceHolder1$txtCardNo03" type="password" maxlength="4" id="ctl00_ContentPlaceHolder1_txtCardNo03" class="input_01" title="카드번호 세번째자리" onkeypress="fn_CheckNumberTextBox(event);" onkeyup="fn_NextFocus('txtCardNo03', 'txtCardNo04', 4)" style="width:50px;text-align:right;">
                                        <input name="ctl00$ContentPlaceHolder1$txtCardNo04" type="text" maxlength="4" id="ctl00_ContentPlaceHolder1_txtCardNo04" class="input_01" title="카드번호 마지막 자리" onkeypress="fn_CheckNumberTextBox(event);" onkeyup="fn_NextFocus('txtCardNo04', 'ddlExpDateYear', 4)" style="width:50px;text-align:right;">
                                    </td>
                                    <td width="38%">
                                        <img src="/images/popup/btn_card_info.gif" alt="무이자 할부 및 혜택 안내" border="0" onclick="fn_OpenModaless('/RSV/PUCard_Info.html','cinfo', '516', '650', 'no');" style="cursor: pointer;">&nbsp;<img src="/images/popup/btn_cpCard_info.gif" alt="법인카드 사용시 주의사항" border="0" onclick="fn_OpenModaless('/RSV/CPCard_Info.htm','cpinfo','475','266', 'no');" style="cursor: pointer;"></td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td height="30" class="Mpurple" style="padding-left: 20px">
                                        <label for="ctl00_ContentPlaceHolder1_installmentPrivateCard" id="ctl00_ContentPlaceHolder1_Label7">할부선택</label>
                                    </td>
                                    <td colspan="2">
                                        <select name="ctl00$ContentPlaceHolder1$installmentPrivateCard" id="ctl00_ContentPlaceHolder1_installmentPrivateCard" style="width: 105px; font-size: 12px; color: #666">
		<option selected="selected" value="00">일시불</option>
		<option value="02">2개월</option>
		<option value="03">3개월</option>
		<option value="04">4개월</option>
		<option value="05">5개월</option>
		<option value="06">6개월</option>
		<option value="07">7개월</option>
		<option value="08">8개월</option>
		<option value="09">9개월</option>
		<option value="10">10개월</option>
		<option value="11">11개월</option>
		<option value="12">12개월</option>
	</select>
                                    </td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td height="30" class="Mpurple" style="padding-left: 20px">유효기간</td>
                                    <td colspan="2">
                                        <select name="ctl00$ContentPlaceHolder1$ddlExpDateYear" id="ctl00_ContentPlaceHolder1_ddlExpDateYear" title="유효기간 년" style="color: #666666; font-size: 9pt; border: solid 1;">
		<option value="">-년-</option>

	</select>
                                        <select name="ctl00$ContentPlaceHolder1$ddlExpDateMonth" id="ctl00_ContentPlaceHolder1_ddlExpDateMonth" title="유효기간 월" style="color: #666666; font-size: 9pt; border: solid 1;">
		<option value="">-월-</option>
		<option value="01">01월</option>
		<option value="02">02월</option>
		<option value="03">03월</option>
		<option value="04">04월</option>
		<option value="05">05월</option>
		<option value="06">06월</option>
		<option value="07">07월</option>
		<option value="08">08월</option>
		<option value="09">09월</option>
		<option value="10">10월</option>
		<option value="11">11월</option>
		<option value="12">12월</option>

	</select>
                                    </td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td height="30" class="Mpurple" style="padding-left: 20px">
                                        <label for="ctl00_ContentPlaceHolder1_txtCardPasswd" id="ctl00_ContentPlaceHolder1_Label8">비밀번호</label></td>
                                    <td colspan="2" style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">
                                        <input name="ctl00$ContentPlaceHolder1$txtCardPasswd" type="password" maxlength="2" id="ctl00_ContentPlaceHolder1_txtCardPasswd" class="input_01" onkeypress="fn_CheckNumberTextBox(event);" onkeyup="fn_NextFocus('txtCardPasswd', 'txtAuthNo', 2)" style="width:50px;text-align:right;">
                                        * 앞 두자리
                                    </td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td height="30" class="Mpurple" style="padding-left: 20px">
                                        <label for="ctl00_ContentPlaceHolder1_txtAuthNo" id="ctl00_ContentPlaceHolder1_Label9">주민등록번호</label></td>
                                    <td colspan="2" style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">
                                        <input name="ctl00$ContentPlaceHolder1$txtAuthNo" type="password" maxlength="10" id="ctl00_ContentPlaceHolder1_txtAuthNo" class="input_01" onkeypress="fn_CheckNumberTextBox(event);" style="width:100px;text-align:right;">
                                        * 개인:주민등록번호 뒤 7자리, 법인:사업자등록번호 10자리
                                    </td>
                                </tr>
                                <tr>
                                    <td colspan="3" height="1" bgcolor="#cbe39d"></td>
                                </tr>
                            </tbody></table>
                            <table id="tbBankPay" style="display: none;" width="685" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr>
                                    <td height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td style="padding: 12px 0px 12px 20px;">
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">실시간 계좌이체를 사용하여 구매한 항공권을 환불하는 경우, <span class="tit">환불은 영업일 기준으로 최소 하루가 소요</span>됩니다.</td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">실시간 계좌이체를 위한 프로그램이 제대로 설치되어 있지 않은 경우 에러가 발생할 수 있습니다.
                                                </td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">반드시 <span class="tit">공인인증서</span>를 사용하셔야 합니다.
                                                </td>
                                            </tr>
                                        </tbody></table>
                                    </td>
                                </tr>
                                <tr>
                                    <td height="1" bgcolor="#cbe39d"></td>
                                </tr>
                            </tbody></table>
                            <table id="tbKakaoPay" style="display: none;" width="685" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr>
                                    <td height="1" bgcolor="#cbe39d"></td>
                                </tr>
                                <tr>
                                    <td style="padding: 12px 0px 12px 20px;">
                                        <table border="0" cellpadding="0" cellspacing="0">
                                            <tbody><tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">현재 국내발행 카드에 한해 결제하실 수 있습니다.</td>
                                            </tr>
                                            <tr>
                                                <td width="10">
                                                    <img src="/images/arrow.gif" alt=""></td>
                                                <td style="font-size: 11px; color: #727272; letter-spacing: -1px; line-height: 18px;">휴대폰에 카카오톡이 설치 되지 않은 경우에는 결제가 정상적으로 진행되지 않습니다.
                                                </td>
                                            </tr>
                                        </tbody></table>
                                    </td>
                                </tr>
                                <tr>
                                    <td height="1" bgcolor="#cbe39d"></td>
                                </tr>
                            </tbody></table>
                            <table id="tbCash" style="display: none;" width="685" border="0" cellspacing="0" cellpadding="0">
                                <tbody><tr>
                                    <td></td>
                                </tr>
                            </tbody></table>
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr>
            <td style="height: 10px;"></td>
        </tr>
        <tr align="center">
            <td>
                <table width="685">
                    <tbody>
                        
                        <tr>
                            <td>
                                
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="ac">
                                
                            </td>
                        </tr>
                        <tr>
                            <td colspan="3" class="ac">
                                
                            </td>
                        </tr>
                    </tbody>
                </table>
            </td>
        </tr>
        <tr>
            <td height="10px"></td>
        </tr>
        <tr align="center">
            <td>
                <table width="685">
                    <tbody><tr>
                        <td id="ctl00_ContentPlaceHolder1_tdValidationInfo"></td>

                    </tr>
                </tbody></table>
            </td>
        </tr>
        <tr>
            <td height="10px"></td>
        </tr>
        <tr id="ctl00_ContentPlaceHolder1_trPayment2" align="center" style="display:none;">
	<td>
                <table width="685">
                    <tbody><tr valign="bottom">
                        <td align="right">
                            <input type="image" name="ctl00$ContentPlaceHolder1$btnPrevApprove" id="ctl00_ContentPlaceHolder1_btnPrevApprove" src="/images/RSV_pre_btn.gif" alt="이전" onclick="return fn_GoScheduleSelect();" style="border-width:0px;">
                            <input type="image" name="ctl00$ContentPlaceHolder1$ibtnApprove" id="ctl00_ContentPlaceHolder1_ibtnApprove" src="../images/RSV_purchase_btn.gif" alt="구매하기" onclick="if(!ClickBtnApproval()) return false;" style="border-width:0px;">
                            <input type="submit" name="ctl00$ContentPlaceHolder1$btnConfirm" value="카드예약완료" id="ctl00_ContentPlaceHolder1_btnConfirm" style="display:none;">
                            
                            
                            <input type="submit" name="ctl00$ContentPlaceHolder1$btnCashConfirm" value="현금예약완료" id="ctl00_ContentPlaceHolder1_btnCashConfirm" style="display:none;">
                            
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr id="ctl00_ContentPlaceHolder1_trApproveGroup" align="center" style="display:none;">
	<td>
                <table width="685">
                    <tbody><tr>
                        <td align="right">
                            <input type="image" name="ctl00$ContentPlaceHolder1$btnPrevGroup" id="ctl00_ContentPlaceHolder1_btnPrevGroup" src="/images/RSV_pre_btn.gif" alt="이전" onclick="return fn_GoScheduleSelect();" style="border-width:0px;">
                            <input type="image" name="ctl00$ContentPlaceHolder1$ibtnApproveGroup" id="ctl00_ContentPlaceHolder1_ibtnApproveGroup" alt="예약신청" disabled="true" src="../images/rsv_appli_btn.gif" onclick="if(!fn_Validation_Group()) return false;" style="border-width:0px;">
                        </td>
                    </tr>
                </tbody></table>
            </td>
</tr>

        <tr>
            <td>
                <input id="price" type="hidden" name="price" style="width: 1px;" value="">
                
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvReqType" id="ctl00_ContentPlaceHolder1_hdnEvReqType">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvCardAmt" id="ctl00_ContentPlaceHolder1_hdnEvCardAmt">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvCardNo" id="ctl00_ContentPlaceHolder1_hdnEvCardNo">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvInstallPeriod" id="ctl00_ContentPlaceHolder1_hdnEvInstallPeriod">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvCavv" id="ctl00_ContentPlaceHolder1_hdnEvCavv">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvXid" id="ctl00_ContentPlaceHolder1_hdnEvXid">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvEci" id="ctl00_ContentPlaceHolder1_hdnEvEci">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvKvpCardcode" id="ctl00_ContentPlaceHolder1_hdnEvKvpCardcode">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvKvpSessionKey" id="ctl00_ContentPlaceHolder1_hdnEvKvpSessionKey">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvKvpEcnData" id="ctl00_ContentPlaceHolder1_hdnEvKvpEcnData">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvKvpPgid" id="ctl00_ContentPlaceHolder1_hdnEvKvpPgid">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEvExpireDate" id="ctl00_ContentPlaceHolder1_hdnEvExpireDate">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnEpMallId" id="ctl00_ContentPlaceHolder1_hdnEpMallId">

                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidBankPay" id="ctl00_ContentPlaceHolder1_hidBankPay">

                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidADiscountInfoOW" id="ctl00_ContentPlaceHolder1_hidADiscountInfoOW">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidADiscountInfoRT" id="ctl00_ContentPlaceHolder1_hidADiscountInfoRT">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidSpclAuth" id="ctl00_ContentPlaceHolder1_hidSpclAuth">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidTmpSpclAuth" id="ctl00_ContentPlaceHolder1_hidTmpSpclAuth">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidPageMode" id="ctl00_ContentPlaceHolder1_hidPageMode" value="INS">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidCompanyAuth" id="ctl00_ContentPlaceHolder1_hidCompanyAuth">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidOperateMode" id="ctl00_ContentPlaceHolder1_hidOperateMode" value="ON">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidPurchaseBtnClick" id="ctl00_ContentPlaceHolder1_hidPurchaseBtnClick">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidMbrGb" id="ctl00_ContentPlaceHolder1_hidMbrGb" value="N">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidIsUnPaidCash" id="ctl00_ContentPlaceHolder1_hidIsUnPaidCash" value="N">
                <input type="hidden" name="ctl00$ContentPlaceHolder1$hidOnlyChild" id="ctl00_ContentPlaceHolder1_hidOnlyChild" value="N">
            </td>
        </tr>
    </tbody></table>
    <span id="divKvp"></span>

    <script type="text/javascript">
        function setCookie(name, value, expiredays) {
            var todayDate = new Date();
            todayDate.setDate(todayDate.getDate() + expiredays);
            document.cookie = name + "=" + escape(value) + "; path=/; expires=" + todayDate.toGMTString() + ";"
        }

        function getCookie(name) {
            var nameOfCookie = name + "=";
            var x = 0;
            while (x <= document.cookie.length) {
                var y = (x + nameOfCookie.length);
                if (document.cookie.substring(x, y) == nameOfCookie) {
                    if ((endOfCookie = document.cookie.indexOf(";", y)) == -1)
                        endOfCookie = document.cookie.length;
                    return unescape(document.cookie.substring(y, endOfCookie));
                }
                x = document.cookie.indexOf(" ", x) + 1;
                if (x == 0)
                    break;
            }
            return "";
        }
    </script>


    <div id="divBackgroud" style="position: absolute; display: none; z-index: 100;">
    </div>

    <div id="divPointUse" style="position: absolute; display: none; z-index: 101;">
        <table width="500" border="0" cellspacing="0" cellpadding="0">
            <tbody><tr>
                <td colspan="3">
                    <img src="/images/RSV_02/pop_top.jpg" border="0" alt="항공운임의 100%가 수수효 적용결제로 진행됩니다. 일반 결제는 10원 단위에서 올림 적용되며, 수수료 적용은 10원 단위에서 내림 적용됩니다."></td>
            </tr>
            <tr>
                <td width="11" bgcolor="#bdd618"></td>
                <td width="478" align="center" bgcolor="#FFFFFF">
                    <table width="440" border="0" cellspacing="0" cellpadding="0">
                        <tbody><tr>
                            <td height="15" colspan="4"></td>
                        </tr>
                        <tr>
                            <td height="1" colspan="4" bgcolor="#bdd618"></td>
                        </tr>
                        <tr>
                            <td height="8" colspan="4"></td>
                        </tr>
                        <tr>
                            <td width="150" class="t01">항공 운임</td>
                            <td width="105" class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblFareOW"></span>
                            </td>
                            <td width="85" class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblFareRT"></span>
                            </td>
                            <td width="100" class="t02">
                                <strong>
                                    <span id="ctl00_ContentPlaceHolder1_lblFareAmt"></span></strong></td>
                        </tr>
                        <tr>
                            <td class="t01">지불 금액</td>
                            <td class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblPointUseOW"></span>
                            </td>
                            <td class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblPointUseRT"></span>
                            </td>
                            <td class="t02">
                                <strong>
                                    <span id="ctl00_ContentPlaceHolder1_lblPointUseAmt"></span></strong></td>
                        </tr>
                        <tr>
                            <td class="t01">수수료</td>
                            <td class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblPointOW"></span>
                            </td>
                            <td class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblPointRT"></span>
                            </td>
                            <td class="t02">
                                <strong>
                                    <span id="ctl00_ContentPlaceHolder1_lblPointAmt"></span></strong></td>
                        </tr>
                        <tr>
                            <td height="6" colspan="4"></td>
                        </tr>
                        <tr>
                            <td height="1" colspan="4" bgcolor="#bdd618"></td>
                        </tr>
                        <tr>
                            <td height="8" colspan="4"></td>
                        </tr>
                        <tr>
                            <td class="t01">잔여 수수료</td>
                            <td colspan="3" class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblRemainPoint"></span></td>
                        </tr>
                        <tr>
                            <td class="t01">사용 수수료</td>
                            <td colspan="3" class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblUsePoint"></span></td>
                        </tr>
                        <tr>
                            <td class="t01">사용 후 잔여</td>
                            <td colspan="3" class="t02">
                                <span id="ctl00_ContentPlaceHolder1_lblAfterReaminPoint"></span></td>
                        </tr>
                        <tr>
                            <td height="6" colspan="4"></td>
                        </tr>
                        <tr>
                            <td height="1" colspan="4" bgcolor="#bdd618"></td>
                        </tr>
                        <tr>
                            <td height="40" colspan="4" align="center">
                                <img src="/images/RSV_02/pop_txt.jpg" border="0" alt="수수료를 적용하시겠습니까?"></td>
                        </tr>
                        <tr>
                            <td colspan="4" align="center">
                                <img src="/images/confirm_btn02.gif" border="0" style="cursor: pointer;" onclick="javascript:PointUseDiv('Y');">&nbsp;
                                <img src="/images/cancel_btn02.gif" width="51" height="28" border="0" style="cursor: pointer;" onclick="javascript:PointUseDiv('N');"></td>
                        </tr>
                    </tbody></table>
                </td>
                <td width="11" bgcolor="#bdd618"></td>
            </tr>
            <tr>
                <td colspan="3">
                    <img src="/images/RSV_02/pop_bottom.jpg" border="0" alt=""></td>
            </tr>
        </tbody></table>
    </div>
    <div id="divPointCancel" style="position: absolute; display: none; z-index: 104;">
        <table width="300" border="0" cellspacing="0" cellpadding="0" bgcolor="#bdd618">
            <tbody><tr>
                <td height="11" colspan="3"></td>
            </tr>
            <tr>
                <td width="11"></td>
                <td>
                    <table width="100%" border="0" cellspacing="0" cellpadding="0" bgcolor="#FFFFFF">
                        <tbody><tr>
                            <td width="18" height="110" valign="top">
                                <img src="/images/PURefund_line01_pop.gif" border="0" alt=""></td>
                            <td rowspan="2" align="center">
                                <p>
                                    수수료 적용을 취소하시겠습니까?
                                </p>
                                <br>
                                <a href="javascript:void(0);" onclick="javascript:PointCancelDiv('Y');">
                                    <img src="/images/confirm_btn02.gif" border="0" style="cursor: pointer;" alt="확인">&nbsp;
                                </a>
                                <a href="javascript:void(0);" onclick="javascript:PointCancelDiv('N');">
                                    <img src="/images/cancel_btn02.gif" border="0" style="cursor: pointer;" alt="취소">
                                </a>
                            </td>
                            <td width="18" valign="top">
                                <img src="/images/PURefund_line03_2_pop.gif" border="0" alt=""></td>
                        </tr>
                        <tr>
                            <td>
                                <img src="/images/PURefund_line04_pop.gif" border="0" alt=""></td>
                            <td>
                                <img src="/images/PURefund_line05_pop.gif" border="0" alt=""></td>
                        </tr>
                    </tbody></table>
                </td>
                <td width="11"></td>
            </tr>
            <tr>
                <td height="11" colspan="3"></td>
            </tr>
        </tbody></table>
    </div>
    <input type="hidden" id="KakaoAuthResult" name="KakaoAuthResult">
    <input type="hidden" id="Amt" name="Amt">
    <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnPayParams" id="ctl00_ContentPlaceHolder1_hdnPayParams">
    <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnKKAOAmt" id="ctl00_ContentPlaceHolder1_hdnKKAOAmt">
    <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnBuyerName" id="ctl00_ContentPlaceHolder1_hdnBuyerName">
    <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnOnlyChild" id="ctl00_ContentPlaceHolder1_hdnOnlyChild">
    <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnParentsPnr" id="ctl00_ContentPlaceHolder1_hdnParentsPnr">
    <input type="hidden" name="ctl00$ContentPlaceHolder1$hdnParentsName" id="ctl00_ContentPlaceHolder1_hdnParentsName">

                    </td>
                </tr>
            </tbody></table>
        </div>
        <div id="banner">
            <p class="first">
                <a href="http://greenwings.jinair.com/" target="_blank">
                    <img src="/images/newMain/greenwings_banner.png" alt="GREENWINGS 진에어 그린윈스 새 창"></a>
            </p>
            <p>
                <a href="javascript:GreenDonation();">
                    <img src="/images/newMain/banner_121220.jpg" alt="GREEN DONATION with Green Cross Korea 진에어가 환경을 사랑하는 마음을 담아 Green Cross Korea를 후원합니다. Green Cross Korea 자세히 보기 새 창"></a>
            </p>
            <p>
                <a href="http://www.jinair.com/HOM/Notice/NoticeView.aspx?seq=15759">
                    <img src="/images/newMain/banner_now.jpg" alt="마감임박 초특가 항공권, 지금 이순간"></a>
            </p>
            <p class="last">
                <a href="javascript:fn_OpenWindow('/HOM/Notice/html/ISMSPopup.html', '정보보호관리체계(ISMS)인증', '608', '867', 'no', false);">
                    <img src="/images/newMain/isms.jpg" alt="정보보호관리체계(ISMS)인증">
                </a>
            </p>
        </div>
        <div id="footer">
            <ul>
                <li id="liPrivacy" class="first"><a href="/User/HompageArticle.aspx">
                    <img src="/images/newMain/footer_01.gif" alt="홈페이지 이용약관"></a></li>
                <li class="boxShow"><a href="#">
                    <img id="imgTransportTerms" src="/images/newMain/footer_02.gif" alt="운송약관"></a>
                    <ul>
                        <li><a href="javascript:GetTransportTerms('DOM');">
                            <img src="/images/newMain/footer_02_over1.png" alt="국내여객운송약관 새 창"></a></li>
                        <li><a href="javascript:GetTransportTerms('INTER');">
                            <img src="/images/newMain/footer_02_over2.png" alt="국제여객운송약관 새 창"></a></li>
                    </ul>
                </li>
                <li><a href="/User/InformationPrivacy.aspx">
                    <img src="/images/newMain/footer_03.gif" alt="개인정보처리방침"></a></li>
                <li><a href="http://jinair.career.co.kr/jobs/" target="_blank">
                    <img src="/images/newMain/footer_04.gif" alt="채용정보 새 창"></a></li>
                <li id="ctl00_liGotoMobileWeb"><a href="javascript:GotoMobileWeb();">
                        <img src="/images/newMain/footer_07.gif" alt="모바일웹"></a></li>
                <li>
                    <img src="/images/newMain/footer_05_new.gif" alt="고객서비스센터 1600-6200/02-3660-6000(오전:6:00~오후8:00)"></li>
            </ul>
            <div class="copy">
                <img src="/images/newMain/footer_copy_new.gif" alt="(주)진에어 대표이사 최정호 외 1명 사업자등록번호 121-81-89086 통신판매업 신고번호: 제2008-서울 강서-0408 주소:서울시 강서구 공항대로 453 개인정보보호 책임자:이광 Copyright © JIN AIR. All rights reserved.">
            </div>
        </div>
        <input type="submit" name="ctl00$btnChangeLanguage" value="" id="ctl00_btnChangeLanguage" style="visibility: hidden;">
        <script type="text/javascript">
            (function (i, s, o, g, r, a, m) {
                i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
                    (i[r].q = i[r].q || []).push(arguments)
                }, i[r].l = 1 * new Date(); a = s.createElement(o),
                m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
            })(window, document, 'script', '//www.google-analytics.com/analytics.js', 'ga');

            ga('create', 'UA-27193049-1', 'auto');
            ga('send', 'pageview');

            $(document).ready(function () {
                if ($("#" + "ctl00_liGotoMobileWeb").length > 0) {
                    $("#liPrivacy").attr("style", "padding-left:150px");
                }
                else {
                    $("#liPrivacy").attr("style", "padding-left:180px");
                }
            });

            function GotoMobileWeb() {
                var operationMode = "ON";
                if (operationMode == "OFF")
                    document.location = "http://wwwstg.jinair.com:8082/MobileWeb/Default.aspx?Language=KOR|KRW";
                else
                    document.location = "https://m.jinair.com/MobileWeb/Default.aspx?Language=KOR|KRW";
            };
        </script>
    

<script type="text/javascript">
//<![CDATA[
fn_FillPaxList();
fn_SetFlightTable_Height();
fn_FlightTable_Visible( 'ctl00_ContentPlaceHolder1_fltlstDownLine' );
GetObj("ctl00_ContentPlaceHolder1_fltlstDownLine_btnInitialized").click();fn_FlightTable_Visible( 'ctl00_ContentPlaceHolder1_fltlstUpLine' );
Sys.Application.initialize();
//]]>
</script>
</form>

</body><div></div></html>"""



from BeautifulSoup import BeautifulSoup

soup = BeautifulSoup(doc)



print soup.findAll("tbody")


































