import os

# 获取当前脚本所在的文件夹
current_folder = os.path.dirname(os.path.abspath(__file__))

# 你想插入到第一行之后的代码
header_code = """<!doctype html>
<html class="no-js" lang="en">

<head>
    <meta charset="utf-8">
    <meta http-equiv="x-ua-compatible" content="ie=edge">
    <title>H&W</title>
    <meta name="description" content="H&W Technology">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    
    <!-- Favicon -->
    <link rel="shortcut icon" type="image/x-icon" href="../../img/favicon.png">
    
    <!-- CSS Files -->
    <!-- Load essential styles first -->
    <link rel="stylesheet" href="../../css/bootstrap.min.css">
    
    <!-- Third-party Libraries CSS -->
    <link rel="stylesheet" href="../../css/font-awesome.min.css">
    <link rel="stylesheet" href="../../css/themify-icons.css">
    <link rel="stylesheet" href="../../css/nice-select.css">

    <!-- Custom CSS -->
    <link rel="stylesheet" href="../../css/style.css">

    <!-- Optional Libraries (If you use them, keep them; otherwise, remove) -->
    <link rel="stylesheet" href="../../css/owl.carousel.min.css">
    <link rel="stylesheet" href="../../css/magnific-popup.css">
    <link rel="stylesheet" href="../../css/gijgo.css">
    <link rel="stylesheet" href="../../css/animate.css">
    <link rel="stylesheet" href="../../css/slick.css">
    <link rel="stylesheet" href="../../css/slicknav.css">
    
    <!-- jQuery UI (if needed) -->
    <link rel="stylesheet" href="https://ajax.googleapis.com/ajax/libs/jqueryui/1.11.2/themes/smoothness/jquery-ui.css">
    <!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
    new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
    j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
    'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
    })(window,document,'script','dataLayer','GTM-M9GM3R54');</script>
    <!-- End Google Tag Manager -->

    <!-- START - We recommend to place the below code in head tag of your website html  -->
<style>
    @font-face {
      font-display: block;
      font-family: Roboto;
      src: url(https://assets.brevo.com/font/Roboto/Latin/normal/normal/7529907e9eaf8ebb5220c5f9850e3811.woff2) format("woff2"), url(https://assets.brevo.com/font/Roboto/Latin/normal/normal/25c678feafdc175a70922a116c9be3e7.woff) format("woff")
    }
  
    @font-face {
      font-display: fallback;
      font-family: Roboto;
      font-weight: 600;
      src: url(https://assets.brevo.com/font/Roboto/Latin/medium/normal/6e9caeeafb1f3491be3e32744bc30440.woff2) format("woff2"), url(https://assets.brevo.com/font/Roboto/Latin/medium/normal/71501f0d8d5aa95960f6475d5487d4c2.woff) format("woff")
    }
  
    @font-face {
      font-display: fallback;
      font-family: Roboto;
      font-weight: 700;
      src: url(https://assets.brevo.com/font/Roboto/Latin/bold/normal/3ef7cf158f310cf752d5ad08cd0e7e60.woff2) format("woff2"), url(https://assets.brevo.com/font/Roboto/Latin/bold/normal/ece3a1d82f18b60bcce0211725c476aa.woff) format("woff")
    }
  
    #sib-container input:-ms-input-placeholder {
      text-align: left;
      font-family: Helvetica, sans-serif;
      color: #c0ccda;
    }
  
    #sib-container input::placeholder {
      text-align: left;
      font-family: Helvetica, sans-serif;
      color: #c0ccda;
    }
  
    #sib-container textarea::placeholder {
      text-align: left;
      font-family: Helvetica, sans-serif;
      color: #c0ccda;
    }
    #sib-container a {
      text-decoration: underline;
      color: #2BB2FC;
    }
    .thumb img {
            width: 100%; /* 默认自适应 */
            height: auto;
        }

        @media (min-width: 768px) {
            .thumb img {
                width: 300px;
                height: 300px;
                object-fit: cover;
            }
        }
  </style>
  <link rel="stylesheet" href="https://sibforms.com/forms/end-form/build/sib-styles.css">
  <!--  END - We recommend to place the above code in head tag of your website html -->
</head>

<body>
    <!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-M9GM3R54"
    height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
    <!-- End Google Tag Manager (noscript) -->
    <header>
        <div class="header-area">
            <div id="sticky-header" class="main-header-area">
                <div class="container-fluid">
                    <div class="header_bottom_border">
                        <div class="row align-items-center">
                            <!-- Logo 部分 -->
                            <div class="col-xl-2 col-lg-2 col-md-12">
                                <div class="logo text-center">
                                    <a href="../../index.html">
                                        <img src="../../img/logo.png" alt="Logo">
                                    </a>
                                </div>
                            </div>

                            <!-- 导航菜单部分，使用 Bootstrap 响应式导航 -->
                            <div class="col-xl-6 col-lg-6">
                                <nav class="navbar navbar-expand-lg navbar-light">
                                    <a class="navbar-brand" href="../../index.html"></a>
                                    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                                        <span class="navbar-toggler-icon"></span>
                                    </button>
                                    <div class="collapse navbar-collapse" id="navbarNav">
                                        <ul class="navbar-nav">
                                            <li class="nav-item">
                                                <a class="nav-link active" href="../../index.html">Home</a>
                                            </li>
                                            <li class="nav-item dropdown">
                                                <a class="nav-link dropdown-toggle" href="#" id="categoriesDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                                                    Categories
                                                </a>
                                                <div class="dropdown-menu" aria-labelledby="categoriesDropdown">
                                                    <a class="dropdown-item" href="../../automation.html">Automation</a>
                                                    <a class="dropdown-item" href="../../cnc.html">CNC</a>
                                                    <a class="dropdown-item" href="../../equipment.html">Equipment</a>
                                                    <a class="dropdown-item" href="../../others.html">Others</a>
                                                    <!-- 其他菜单项 -->
                                                </div>
                                            </li>
                                            <li class="nav-item dropdown">
                                            </li>
                                            <li class="nav-item">
                                                <a class="nav-link" href="../../contact.html">Contact</a>
                                            </li>
                                            <li class="nav-item">
                                                <a class="nav-link" href="../../about.html">About</a>
                                            </li>
                                        </ul>
                                    </div>
                                </nav>
                            </div>

                            <!-- 联系方式和社交媒体 -->
                            <div class="col-xl-4 col-lg-4">
                                <div class="social_wrap d-flex align-items-center justify-content-end">
                                    <div class="number" style="text-align: right;">
                                        <p> <i class="fa fa-phone"></i> CONTACT US</p>
                                    </div>
                                    <div class="social_links">
                                        <ul class="d-flex">
                                            <li><a href="https://wa.me/message/ZOIEJJTNPJ75H1?src=qr"> <i class="fa fa-whatsapp"></i> </a></li>
                                            <li><a href="https://www.linkedin.com/company/hangnwen"> <i class="fa fa-linkedin"></i> </a></li>
                                            <li><a href="https://www.instagram.com/guan_hang/"> <i class="fa fa-instagram"></i> </a></li>
                                            <li><a href="http://www.youtube.com/@Hangnwen"> <i class="fa fa-youtube-play"></i> </a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div> <!-- .row 结束 -->
                    </div> <!-- .header_bottom_border 结束 -->
                </div> <!-- .container-fluid 结束 -->
            </div> <!-- #sticky-header 结束 -->
        </div> <!-- .header-area 结束 -->
    </header>
</body>\n"""  # 末尾加换行符，确保格式美观

# 你想插入到文件末尾的代码
footer_code = """\n    <style>
        /* 响应式布局 */
        @media (max-width: 768px) {
            .product-item {
                flex-direction: column; /* 在小屏幕上改为垂直布局 */
            }
            .product-item > div {
                margin-right: 0; /* 移除图片的右边距 */
                margin-bottom: 20px; /* 增加图片与信息之间的间距 */
            }
            .product-item img {
                max-width: 100%; /* 确保图片在小屏幕上不会溢出 */
            }
        }
    </style>

    <script>
        // 筛选功能
        const checkboxes = document.querySelectorAll('.brand-filter');
        const products = document.querySelectorAll('.product-item');

        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', () => {
                const selectedBrands = Array.from(checkboxes)
                    .filter(cb => cb.checked)
                    .map(cb => cb.value);

                products.forEach(product => {
                    const productBrand = product.getAttribute('data-brand');
                    if (selectedBrands.length === 0 || selectedBrands.includes(productBrand)) {
                        product.style.display = 'block';
                    } else {
                        product.style.display = 'none';
                    }
                });
            });
        });
    </script>
</body>


</body>
        <!-- Brevo Conversations {literal} -->
        <script>
            (function(d, w, c) {
                w.BrevoConversationsID = '670cd442f718268d2509c87b';
                w[c] = w[c] || function() {
                    (w[c].q = w[c].q || []).push(arguments);
                };
                var s = d.createElement('script');
                s.async = true;
                s.src = 'https://conversations-widget.brevo.com/brevo-conversations.js';
                if (d.head) d.head.appendChild(s);
            })(document, window, 'BrevoConversations');
        </script>
        <!-- /Brevo Conversations {/literal} -->

    <footer class="footer">
        <div class="footer_top">
            <div class="container">
                <div class="row">
                    <!-- 公司信息部分 -->
                    <div class="col-xl-4 col-md-6 col-lg-4 ">
                        <div class="footer_widget">
                            <div class="footer_logo">
                                <a href="https://hangandwen.com/">
                                    <img src="../../img/footer_logo.png" alt="Company Logo" style="max-width: 150px;">
                                </a>
                            </div>
                            <p>
                                H&W Education Technology (Shenzhen) Co., Ltd. <br>
                                59 Building 3, Mingju Plaza, Longgang District, Shenzhen, China.<br>
                                <a href="https://wa.me/message/ZOIEJJTNPJ75H1?src=qr">+86 17707252369</a> <br>
                                <a href="mailto:Info@hangnwen.com">Info@hangnwen.com</a>
                            </p>
                            <div class="socail_links">
                                <ul style="padding-left: 0;">
                                    <li style="display: inline-block; margin-right: 10px;">
                                        <a href="https://wa.me/message/ZOIEJJTNPJ75H1?src=qr">
                                            <i class="fa fa-whatsapp"></i>
                                        </a>
                                    </li>
                                    <li style="display: inline-block; margin-right: 10px;">
                                        <a href="https://www.linkedin.com/company/hangnwen">
                                            <i class="ti-linkedin"></i>
                                        </a>
                                    </li>
                                    <li style="display: inline-block; margin-right: 10px;">
                                        <a href="https://www.instagram.com/guan_hang/">
                                            <i class="fa fa-instagram"></i>
                                        </a>
                                    </li>
                                    <li style="display: inline-block;">
                                        <a href="http://www.youtube.com/@Hangnwen">
                                            <i class="fa fa-youtube-play"></i>
                                        </a>
                                    </li>
                                </ul>
                            </div>
                        </div>
                    </div>
                    

                                      <!-- START - We recommend to place the below code where you want the form in your website html  -->
  <div class="sib-form" style="text-align: center;
  background-color: #EFF2F7;                                 ">
<div id="sib-form-container" class="sib-form-container">
<div id="error-message" class="sib-form-message-panel" style="font-size:16px; text-align:left; font-family:Helvetica, sans-serif; color:#661d1d; background-color:#ffeded; border-radius:3px; border-color:#ff4949;max-width:540px;">
<div class="sib-form-message-panel__text sib-form-message-panel__text--center">
 <svg viewBox="0 0 512 512" class="sib-icon sib-notification__icon">
   <path d="M256 40c118.621 0 216 96.075 216 216 0 119.291-96.61 216-216 216-119.244 0-216-96.562-216-216 0-119.203 96.602-216 216-216m0-32C119.043 8 8 119.083 8 256c0 136.997 111.043 248 248 248s248-111.003 248-248C504 119.083 392.957 8 256 8zm-11.49 120h22.979c6.823 0 12.274 5.682 11.99 12.5l-7 168c-.268 6.428-5.556 11.5-11.99 11.5h-8.979c-6.433 0-11.722-5.073-11.99-11.5l-7-168c-.283-6.818 5.167-12.5 11.99-12.5zM256 340c-15.464 0-28 12.536-28 28s12.536 28 28 28 28-12.536 28-28-12.536-28-28-28z" />
 </svg>
 <span class="sib-form-message-panel__inner-text">
                   Your subscription could not be saved. Please try again.
               </span>
</div>
</div>
<div></div>
<div id="success-message" class="sib-form-message-panel" style="font-size:16px; text-align:left; font-family:Helvetica, sans-serif; color:#085229; background-color:#e7faf0; border-radius:3px; border-color:#13ce66;max-width:540px;">
<div class="sib-form-message-panel__text sib-form-message-panel__text--center">
 <svg viewBox="0 0 512 512" class="sib-icon sib-notification__icon">
   <path d="M256 8C119.033 8 8 119.033 8 256s111.033 248 248 248 248-111.033 248-248S392.967 8 256 8zm0 464c-118.664 0-216-96.055-216-216 0-118.663 96.055-216 216-216 118.664 0 216 96.055 216 216 0 118.663-96.055 216-216 216zm141.63-274.961L217.15 376.071c-4.705 4.667-12.303 4.637-16.97-.068l-85.878-86.572c-4.667-4.705-4.637-12.303.068-16.97l8.52-8.451c4.705-4.667 12.303-4.637 16.97.068l68.976 69.533 163.441-162.13c4.705-4.667 12.303-4.637 16.97.068l8.451 8.52c4.668 4.705 4.637 12.303-.068 16.97z" />
 </svg>
 <span class="sib-form-message-panel__inner-text">
                   Your subscription has been successful.
               </span>
</div>
</div>
<div></div>
<div id="sib-container" class="sib-container--large sib-container--vertical" style="text-align:center; background-color:rgba(255,255,255,1); max-width:540px; border-radius:3px; border-width:1px; border-color:#C0CCD9; border-style:solid; direction:ltr">
<form id="sib-form" method="POST" action="https://5eb2e1ea.sibforms.com/serve/MUIFAOgtpiu9yYh04g6aYHvVCchkgYBen96JEuTwfPf9D36SeS5_LXlozqyufPAQqHv4RnVRfNUgAIKdQcnvmwWtw78kYub4AOH_8MjkI4uDQnjaCksFwK58ebGKSGbdyYvQ1qnIn4pzjvy7PyXNmBzU_ECZpfoYEEM3rZSG1U3Irmmj7hj6eNPZ2WRbtVFFkxtM16oAjbdvkbIM" data-type="subscription">
 <div style="padding: 8px 0;">
   <div class="sib-form-block" style="font-size:32px; text-align:left; font-weight:700; font-family:Helvetica, sans-serif; color:#3C4858; background-color:transparent; text-align:left">
     <p>New Release</p>
   </div>
 </div>
 <div style="padding: 8px 0;">
   <div class="sib-form-block" style="font-size:16px; text-align:left; font-family:Helvetica, sans-serif; color:#3C4858; background-color:transparent; text-align:left">
     <div class="sib-text-form-block">
       <p>Subscribe to our new release list and stay updated.</p>
     </div>
   </div>
 </div>
 <div style="padding: 8px 0;">
   <div class="sib-input sib-form-block">
     <div class="form__entry entry_block">
       <div class="form__label-row ">
         <label class="entry__label" style="font-weight: 700; text-align:left; font-size:16px; text-align:left; font-weight:700; font-family:Helvetica, sans-serif; color:#3c4858;" for="EMAIL" data-required="*">Enter your email address to subscribe</label>

         <div class="entry__field">
           <input class="input " type="text" id="EMAIL" name="EMAIL" autocomplete="off" placeholder="EMAIL" data-required="true" required />
         </div>
       </div>

       <label class="entry__error entry__error--primary" style="font-size:16px; text-align:left; font-family:Helvetica, sans-serif; color:#661d1d; background-color:#ffeded; border-radius:3px; border-color:#ff4949;">
       </label>
       <label class="entry__specification" style="font-size:12px; text-align:left; font-family:Helvetica, sans-serif; color:#8390A4; text-align:left">
         Provide your email address to subscribe. For e.g abc@xyz.com
       </label>
     </div>
   </div>
 </div>
 <div style="padding: 8px 0;">
   <div class="sib-form-block" style="text-align: left">
     <button class="sib-form-block__button sib-form-block__button-with-loader" style="font-size:16px; text-align:left; font-weight:700; font-family:Helvetica, sans-serif; color:#FFFFFF; background-color:#3E4857; border-radius:3px; border-width:0px;" form="sib-form" type="submit">
       <svg class="icon clickable__icon progress-indicator__icon sib-hide-loader-icon" viewBox="0 0 512 512">
         <path d="M460.116 373.846l-20.823-12.022c-5.541-3.199-7.54-10.159-4.663-15.874 30.137-59.886 28.343-131.652-5.386-189.946-33.641-58.394-94.896-95.833-161.827-99.676C261.028 55.961 256 50.751 256 44.352V20.309c0-6.904 5.808-12.337 12.703-11.982 83.556 4.306 160.163 50.864 202.11 123.677 42.063 72.696 44.079 162.316 6.031 236.832-3.14 6.148-10.75 8.461-16.728 5.01z" />
       </svg>
       SUBSCRIBE
     </button>
   </div>
 </div>

 <input type="text" name="email_address_check" value="" class="input--hidden">
 <input type="hidden" name="locale" value="en">
</form>
</div>
</div>
</div>
<!-- END - We recommend to place the above code where you want the form in your website html  -->
    
                    <!-- 其他部分的内容可以继续添加 -->
                </div>
            </div>
        </div>
    
        <div class="copy-right_text">
            <div class="container">
                <div class="footer_border" style="border-top: 1px solid #eaeaea; margin: 20px 0;"></div>
                <div class="row">
                    <div class="col-xl-12">
                        <p class="copy_right text-center">
                            Copyright &copy;<script>document.write(new Date().getFullYear());</script> All rights reserved
                        </p>
                    </div>
                </div>
            </div>
        </div>

                    <!-- Begin Brevo Form -->

  
  <!-- START - We recommend to place the below code in footer or bottom of your website html  -->
  <script>
    window.REQUIRED_CODE_ERROR_MESSAGE = 'Please choose a country code';
    window.LOCALE = 'en';
    window.EMAIL_INVALID_MESSAGE = window.SMS_INVALID_MESSAGE = "The information provided is invalid. Please review the field format and try again.";
  
    window.REQUIRED_ERROR_MESSAGE = "This field cannot be left blank. ";
  
    window.GENERIC_INVALID_MESSAGE = "The information provided is invalid. Please review the field format and try again.";
  
  
  
  
    window.translation = {
      common: {
        selectedList: '{quantity} list selected',
        selectedLists: '{quantity} lists selected'
      }
    };
  
    var AUTOHIDE = Boolean(0);
  </script>
  
  <script defer src="https://sibforms.com/forms/end-form/build/main.js"></script>
  
  
  <!-- END - We recommend to place the above code in footer or bottom of your website html  -->
  <!-- End Brevo Form -->
   
    </footer>

<!-- 保留脚本文件加载部分 -->
<script src="../../js/vendor/modernizr-3.5.0.min.js"></script>
<script src="../../js/vendor/jquery-3.6.0.min.js"></script> 
<script src="../../js/popper.min.js"></script>
<script src="../../js/bootstrap.min.js"></script>
<script src="../../js/owl.carousel.min.js"></script>
<script src="../../js/isotope.pkgd.min.js"></script>
<script src="../../js/ajax-form.js"></script>
<script src="../../js/waypoints.min.js"></script>
<script src="../../js/jquery.counterup.min.js"></script>
<script src="../../js/imagesloaded.pkgd.min.js"></script>
<script src="../../js/scrollIt.js"></script>
<script src="../../js/jquery.scrollUp.min.js"></script>
<script src="../../js/wow.min.js"></script>
<script src="../../js/nice-select.min.js"></script>
<script src="../../js/jquery.slicknav.min.js"></script>
<script src="../../js/jquery.magnific-popup.min.js"></script>
<script src="../../js/plugins.js"></script>
<script src="../../js/gijgo.min.js"></script>
<script src="../../js/slick.min.js"></script>
<script src="../../js/contact.js"></script>
<script src="../../js/jquery.ajaxchimp.min.js"></script>
<script src="../../js/jquery.form.js"></script>
<script src="../../js/jquery.validate.min.js"></script>
<script src="../../js/mail-script.js"></script>
<script src="../../js/main.js"></script>

<!-- Datepicker Initialization -->
<script>
    $('#datepicker').datepicker({
        iconsLibrary: 'fontawesome',
        icons: {
            rightIcon: '<span class="fa fa-caret-down"></span>'
        }
    });
</script>

<!-- Owl Carousel Initialization -->
<script>
    $(document).ready(function(){
        $(".testmonial_active").owlCarousel({
            items: 1,
            loop: true,
            autoplay: true,
            autoplayTimeout: 5000,
            nav: false,
            dots: true
        });
    });
</script>
</body>
</html>"""  # 头部加换行符，确保与原代码分隔

# 遍历当前文件夹中的所有 HTML 文件
for filename in os.listdir(current_folder):
    if filename.endswith(".html"):  # 只处理 HTML 文件
        filepath = os.path.join(current_folder, filename)

        with open(filepath, "r", encoding="utf-8") as file:
            lines = file.readlines()  # 读取所有行

        if lines:  # 确保文件不是空的
            lines.insert(1, header_code)  # 在原代码的第一行后插入 header_code
            lines.append(footer_code)  # 直接在文件末尾插入 footer_code

            with open(filepath, "w", encoding="utf-8") as file:
                file.writelines(lines)  # 重新写入修改后的内容

            print(f"文件 {filename} 已成功更新！")

print("所有 HTML 文件已处理完成！")
