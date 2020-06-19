# Tấn công từ chối dịch vụ

## Sơ lược về DoS

Tấn công từ chối dịch vụ (Denial of Service hay Dos) là kiểu tấn công làm quá tải tài nguyên hệ thống, khiến cho hệ thống chậm đi đáng kể so với người dùng bình thường hoặc khiến hệ thống không thể sử dụng được nữa.

Tuy kẻ tấn công không thể chiếm quyền điều khiển hoặc truy cập dữ liệu trên hệ thống, tuy nhiên tấn công từ chối dịch vụ khiến cho hệ thống hoạt động kém hiệu quả hoặc không hoạt động được, đối với người dùng bình thường  không thể sử dụng dịch vụ do hệ thống cung cấp.

Attacker thường là một hoặc một số máy tính thực hiện nên có thể ngăn chặn dễ dàng bằng cách chặn các gói tin đến từ địa chỉ IP đó.

## Sơ lược về DDoS

![DDoS](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/ddos.png)

Tấn công từ chối dịch vụ phân tán (Distributed Denial of Service hay DDoS) là tấn công từ chối dịch vụ phân tán và là phiên bản nâng cấp của DoS vì rất khó bị ngăn chặn. Hậu quả sau tấn công DDoS là sự sụp đổ của cả một hệ thống máy chủ trực tuyến. DDoS được thực hiện bằng cách tăng lượng truy cập trực tuyến từ nhiều nguồn đến máy chủ. Từ đó khiến máy chủ cạn kiệt tài nguyên lẫn băng thông.

DDoS không chỉ dùng một máy tính để tấn công mà còn lợi dụng hàng triệu máy tính khác, các hệ thống Botnet hoặc các thiết bị IoT. Chúng cộng hưởng lại sẽ tạo ra các “đợt sóng thần” traffic. Do được phân tán thành nhiều điểm truy cập có dải IP khác nhau, DDoS mạnh hơn DoS rất nhiều. Thường rất khó để nhận biết hoặc ngăn chặn các cuộc tấn công DDos.

## Lịch sử các cuộc tấn công DDoS

- Các cuộc tấn công DoS đầu tiên được ghi nhận vào đầu những năm 90, các cuộc tấn công trong thời gian này chủ yếu nhằm làm quá tải băng thông victim, các dạng tấn công thời ký này chủ yếu là **ping floods**, **SYN floods** và **UDP floods**.
- Các dạng tấn công sau đó trở nên phức tạp hơn, mạo danh địa chỉ IP khiến victim không thể cùng lúc trả lời một lượng lớn thông điệp được gửi đến, các dạng tấn công có thể kể đến là **Smurf attack**, **IP spoofing**.
- Các cuộc tấn công ban đầu yêu cầu một lượng attacker đồng bộ thủ công với nhau nhằm gửi một lượng lớn gói tin gây quá tải victim. Tuy nhiên từ năm 1997, với sự ra đời của **Trinoo** là công cụ tấn công DDoS đầu tiên mà các attacker không cần đồng bộ thủ công nữa mà có thể tạo ra các cuộc tấn công song song với quy mô lớn. **Trinoo** hoạt động dựa trên hình thức tấn công UDP floods và các giao tiếp master-slave. Trong các năm tiếp theo, có thêm nhiều công cụ mới ra đời như **TFN** (tribe flood network), **TFN2K**  và **Stacheldraht**.
- Đến cuối năm 1999 đầu năm 2000, tấn công từ chối dịch vụ mới được biết đến rộng rãi sau khi các trang web lớn thời đó đồng loạt bị tấn công với quy mô lớn như **amazon.com**, **cnn.com**, **eBay.com**, **buy.com**, **Yahoo.com**, đỉnh điểm **Yahoo.com** bị tấn công 1GB/s.
- Ngày 15/08/2003, **Microsoft** hứng chịu DDos làm gián đoạn website trong vòng 2 giờ.
- Ngày 27/03/2003, **AI-Jazeera** bị tấn công làm gián đoạn trong nhiều giờ.
- Trong những năm trờ lại đây, các cuộc tấn công DDoS vẫn diễn ra hết sức phức tạp và với quy mô ngày càng lớn. Ở Việt Nam, VCCorp hứng chịu đợt tấn công DDoS gây lỗi hàng loạt data center của các trang báo mạng lớn tại Việt Nam như **Soha**, **Kênh 14**.... Ngày 26/10/2015, **VN-Zoom** bị tấn công với băng thông 400MB/s. Trên thế giới, ngày 28/02/2018, **Github** bị tấn công DDoS với băng thông **1.35Tb/s**, lớn nhất từ trước đến nay.

![Github attack](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/github-ddos.jpg)

## Hậu quả của các cuộc tấn công DDoS

- Gây tiêu tốn tài nguyên hệ thống, gây quá tải băng thông, đầy dung lượng lưu trữ, tăng thời gian xử lý yêu cầu.
- Phá vỡ các thành phần vật lý của mạng máy tính.
- Làm tắc nghẽn thông tin liên lạc ra bên ngoài.
- Phá vỡ các thông tin cấu hình.
- Phá vỡ các trạng thái thông tin như việc tự động reset lại các phiên TCP.
- Làm quá tải năng lực xử lý, dẫn đến hệ thống không thể thực thi bất kì một công việc nào khác.
- Gây Crash hệ thống.
- Tấn công từ chối dịch vụ iFrame: Trong một trang HTML có thể gọi đến một trang web nào đó với rất nhiều yêu cầu và trong rất nhiều lần cho đến khi băng thông của trang web đó bị quá hạn.

Mặc dù phần lớn các cuộc tấn công DDoS đều mang mục đích phá hoại, tuy nhiên, DDoS cũng được sử dụng để

- Street test hệ thống.
- Kiểm thử các lỗ hổng bảo mật, kiểm tra mức độ chống chịu, phát hiện các hình thức tấn công mới.
- Có thêm những hiểu biết, thông tin quan trọng sau các cuộc tấn công DDoS, từ đó phát triển các phương thức phòng thủ, giảm thiểu hậu quả do DDoS gây ra.

## Bot và Botnet

Cuối thế kỷ 19 cũng như đầu thiên niên kỷ mới đánh dấu bước phát triển nhanh, mạnh của một số chiến lược tấn công khác biệt nhắm vào hệ thống mạng. DDoS, tức Distributed Denial of Services, hình thức tấn công từ chối dịch vụ phân tán khét tiếng ra đời. Tương tự với người anh em DoS *(tấn công từ chối dịch vụ)*, DDoS được phát tán rất rộng, chủ yếu nhờ tính đơn giản nhưng rất khó bị dò tìm của chúng. Đã có nhiều kinh nghiệm đối phó được chia sẻ, với khối lượng kiến thức không nhỏ về nó, nhưng ngày nay DDoS vẫn đang là một mối đe doạ nghiêm trọng và là một công cụ nguy hiểm của các hacker. Các cuộc tấn công DDoS thường được triển khai trên một hệ thống các Botnet.

### Bot là gì

Bot là những chương trình tương tự Trojan backdoor cho phép kẻ tấn công sử dụng máy của họ như là những Zoombie *(máy tính thây ma – máy tính bị chiếm quyền điều khiển hoàn toàn)* và chúng chủ động kết nối với một Server để dễ dàng điều khiển Chính vì sự chủ động này mà máy tính bị cài đặt chúng kết nối trở nên chậm chạp , một đặc điểm giúp ta dễ dàng nhận diện bot.

### Botnet là gì

Mạng botnet là một mạng rất lớn gồm hàng trăm hàng ngàn máy tính Zombie kết nối với một máy chủ mIRC *( Internet Replay Chat )* hoặc qua các máy chủ DNS để nhận lệnh từ hacker một cách nhanh nhất. Các mạng bot gồm hàng ngàn *“thành viên”* là một công cụ lý tưởng cho các cuộc chiến tranh đọ máu như DDOS, spam, cài đặt các chương trình quảng cáo…

### Sơ lược về mạng IRC

![irc network](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/irc-mode.jpg)

IRC là tên viết tắt của Internet Relay Chat. Đó là một giao thức được thiết kế cho hoạt động liên lạc theo kiểu hình thức tán gẫu thời gian thực (ví dụ RFC 1459, các bản update RFC 2810, 2811, 2812, 2813) dựa trên kiến trúc client-server. Hầu hết mọi server IRC đều cho phép truy cập miễn phí, không kể đối tượng sử dụng. IRC là một giao thức mạng mở dựa trên nền tảng TCP *(Transmission Control Protocol),* đôi khi được nâng cao với SSL (Secure Sockets Layer).

Một server IRC kết nối với server IRC khác trong cùng một mạng. Người dùng IRC có thể liên lạc với cả hai theo hình thức công cộng *(trên các kênh)* hoặc riêng tư *(một đối một)*. Có hai mức truy cập cơ bản vào kênh IRC: mức người dùng *(user)* và mức điều hành *(operator)*.

Người dùng nào tạo một kênh liên lạc riêng sẽ trở thành người điều hành. Một điều hành viên có nhiều đặc quyền hơn *(tuỳ thuộc vào từng kiểu chế độ do người điều hành ban đầu thiết lập)* so với người dùng thông thường.

Các bot IRC được coi như một người dùng *(hoặc điều hành viên)* thông thường. Chúng là các quy trình daemon, có thể chạy tự động một số thao tác. Quá trình điều khiển các bot này thông thường dựa trên việc gửi lệnh để thiết lập kênh liên lạc do hacker thực hiện, với mục đích chính là phá hoại. Tất nhiên, việc quản trị bot cũng đòi hỏi cơ chế thẩm định và cấp phép. Vì thế, chỉ có chủ sở hữu chúng mới có thể sử dụng.

Các bot đều có tính năng đầy đủ của một trojan và sự kết hợp nhuần nhuyễn từ virus vì vậy các con bot đều có thể tự lây lan thông qua các lỗ hổng của hệ điều hành và chiếm quyền điều khiển máy của người dùng. Ngoài ra một số bot không được tích hợp tính năng lây lan nên nó cần đc sự hộ tống của một virus (đây chính là dạng lây lan phổ biến của các bot hiện nay).

Cách đây chưa lâu, các mạng zombie *(một tên khác của máy tính bị tấn công theo kiểu bot)* thường được điều khiển qua công cụ độc quyền, do chính các hacker phát triển. Trải qua thời gian, chúng hướng tới phương thức điều khiển từ xa. IRC được xem là công cụ phát động các cuộc tấn công tốt nhất nhờ tính linh hoạt, dễ sử dụng và đặc biệt là các server chung có thể được dùng như một phương tiện liên lạc. IRC cung cấp cách thức điều khiển đơn giản hàng trăm, thậm chí hàng nghìn bot cùng lúc một cách linh hoạt. Nó cũng cho phép kẻ tấn công che đậy nhân dạng thật của mình với một số thủ thuật đơn giản như sử dụng proxy nặc danh hay giả mạo địa chỉ IP. Song cũng chính bởi vậy mà chúng để lại dấu vết cho người quản trị server lần theo.

Điển hình ở Việt Nam chúng ta cũng có một mạng botnet IRC tương đối lớn khoảng 1000 zombie rải đều cả nước do Hacker LlyKil người Quảng Nam thực hiện kiển soát và điều khiển để tấn công truongton.net và nhiều website nổi tiếng Việt Nam vào những năm 2008. Và Llykil bị bắt khi vừa thực hiện xong cuộc tấn công và BKAV *(Website chương trình diệt Virus của Việt Nam)* thông qua Botnet bằng kênh chat IRC này.

Trong hầu hết các trường hợp tấn công bởi bot, nạn nhân chủ yếu là người dùng máy tính đơn lẻ, server ở các trường đại học hoặc mạng doanh nghiệp nhỏ. Lý do là bởi máy tính ở những nơi này không được giám sát chặt chẽ và thường để hở hoàn toàn lớp bảo vệ mạng.

Những đối tượng người dùng này thường không xây dựng cho mình chính sách bảo mật, hoặc nếu có thì không hoàn chỉnh, chỉ cục bộ ở một số phần. Hầu hết người dùng máy tính cá nhân kết nối đường truyền ADSL đều không nhận thức được các mối nguy hiểm xung quanh và không sử dụng phần mềm bảo vệ như các công cụ diệt virus hay tường lửa cá nhân.

### Mối quan hệ giữa Botnet và DDoS

Các botnet được sử dụng thường xuyên trong các cuộc tấn công Distributed Denial of Service (DDoS). Một kẻ tấn công có thể điều khiển số lượng lớn máy tính bị chiểm quyền điều khiển tại một trạm từ xa, khai thác băng thông của chúng và gửi yêu cầu kết nối tới máy đích. Và trong một số trường hợp, thủ phạm được tìm thấy ngay khi đang tiến hành cuộc phá hoại *(như ở các cuộc chiến dotcom)*.

Tấn công DDoS là một biến thể của Foolding DoS. Mục đích của hình thức này là gây tràn mạng đích, sử dụng tất cả băng thông có thể. Kẻ tấn công sau đó sẽ có toàn bộ lượng băng thông khổng lồ trên mạng để làm tràn website đích. 

Tất cả sẽ được dùng một lần, và nhờ đó, phân tán được cuộc tấn công vào website đích. Một trong các kiểu tấn công phổ biến nhất được thực hiện thông qua sử dụng giao thức TCP *(một giao thức hướng kết nối)*, gọi là TCP syn flooding. Cách thức hoạt động của chúng là gửi đồng thời cùng lúc một số lượng khổng lồ yêu cầu kết nối TCP tới một web server *(hoặc bất kỳ dịch vụ nào khác)*, gây tràn tài nguyên server, dẫn đến tràn băng thông và ngăn không cho người dùng khác mở kết nối riêng của họ. Quả là đơn giản nhưng thực sự nguy hiểm! Kết quả thu được cũng tương tự khi dùng giao thức UDP *(một giao thức không kết nối)*.

Giới tin tặc cũng bỏ ra khá nhiều thời gian và công sức đầu tư nhằm nâng cao cách thức tấn công của chúng. Hiện nay, người dùng mạng máy tính như chúng ta đang phải đối mặt với nhiều kỹ thuật tinh vi hơn xa so kiểu tấn công DDoS truyền thống. Những kỹ thuật này cho phép kẻ tấn công điều khiển một số lượng cực kỳ lớn máy tính bị chiếm quyền điều khiển *(zombie)* tại một trạm từ xa mà đơn giản chỉ cần dùng giao thức IRC.

### Các dạng bot

#### GT-bot

Tất cả các bot GT *(Global Threat)* đều dựa trên kiểu client IRC phổ biến dành cho Windows gọi là mIRC. Cốt lõi của các bot này là xây dựng tập hợp script mIRC, được dùng để điểu khiển hoạt động của hệ thống từ xa. Kiểu bot này khởi chạy một phiên client nâng cao với các script điều khiển và dùng một ứng dụng thứ hai, thông thường là HideWindows để ẩn mIRC trước người dùng máy tính đích. Một file DLL bổ sung sẽ thêm một số thành phần mới vào mIRC để các script có thể chi phối nhiều khía cạnh khác nhau trên máy tính bị chiếm quyền điều khiển.

#### Agobot

Agobot là một trong những kiểu bot phổ biến nhất thường được các craker chuyên nghiệp sử dụng. Chúng được viết trên nền ngôn ngữ C++ và phát hành dưới dạng bản quyền GPL. Điểm thú vị ở Agobot là mã nguồn. Được modul hoá ở mức cao, Agobot cho phép thêm chức năng mới vào dễ dàng. Nó cũng cung cấp nhiều cơ chế ẩn mình trên máy tính người dùng. Thành phần chính của Agobot gồm: NTFS Alternate Data Stream *(Xếp luân phiên dòng dữ liệu NTFS)*, Antivirus Killer *(bộ diệt chương trình chống virus)* và Polymorphic Encryptor Engine *(cơ chế mã hoá hình dạng).* Agobot cung cấp tính năng sắp xếp và sniff lưu lượng. Các giao thức khác ngoài IRC cũng có thể được dùng để điều khiển kiểu bot này.

#### DSNX

Dataspy Network X (DSNX) cũng được viết trên nền ngồn ngữ C++ và mã nguồn dựa trên bản quyền GPL. Ở kiểu bot này có thêm một tính năng mới là kiến trúc plug-in đơn giản.

#### SDBot

SDBot được viết trên nền ngôn ngữ C và cũng sử dụng bản quyền GPL. Không giống như Agobot, mã nguồn của kiểu bot này rất rõ ràng và bản thân phần mềm có một lượng giới hạn chức năng. Nhưng SDBot rất phổ biến và đã được phát triển ra nhiều dạng biến thể khác nhau.

## Một số hình thức tấn công DDoS cơ bản

- Smurf flood
- Ping of death.
- Teardrop
- SYN attack.
- UDP flood
- HTTP flood
- Application level attack
- NTP amplification

### Smurf flood

Trước khi tim hiểu về cách thức Smurf flood hoạt động, ta cần tìm hiểu về giao thức **ICMP**

#### Internet control message protocol (ICMP)

ICMP hay còn gọi là giao thức điều khiển truyền tin qua mạng Internet, được tạo ra với mục đích báo cáo lỗi, ngay khi có lỗi xảy ra trong quá trình truyền tin, gói tin ICMP sẽ được tạo ra và gửi về cho địa chỉ gửi. Ngoài ra, ICMP còn được dùng để quản lý và thăm dò hoạt động của mạng.

ICMP thường được dùng đẻ:

- Kiểm tra kết nối: khi muốn kiểm tra một máy có tồn tại hoặc hoạt động trong mạng không, ta thường dùng lệnh `ping`, lệnh này dùng để gửi đi một **IMCP echo request** đến máy đích. Khi máy đích nhận được gói tin, nó sẽ gửi lại một **IMCP echo reply**. Máy gửi nhận được gói tin reply có nghĩa là kết nối giữa hai máy hoạt động bình thường.
- Điều khiển dòng dữ liệu: Trong trường hợp gói tin đến máy đích quá nhanh khiến máy đích không kíp xử lý, máy đích sẽ gửi một thông báo về cho máy nguồn tạm ngừng gửi tin để máy đích có thời gian xử lý.
- Nếu không thấy trạm đích thì một thông bao lỗi **ICMP Destination Unreachable** được bộ định tuyến gửi về cho máy gửi.

#### Cách thức tấn công

![irc network](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/smurf-attack.jpg)

Attacker gửi gói tin ICMP request với địa chỉ đích là địa chỉ broadcast (của mạng khuếch đại) và địa chỉ nguồn là địa chỉ của victim. Theo đó thì tất cả các máy nằm trong mạng khuếch đại sẽ đồng loạt trả lời về địa chỉ nguồn (victim) bằng gói tin ICMP reply với đích là máy victim.

Máy victim sẽ không thể xử lý kịp thời một lượng lớn thông tin và dẫn tới bị treo máy. Như vậy chỉ cần một lượng nhỏ các gói tin ICMP đi đến mạng khuếch đại sẽ khuếch đại lượng gói tin lên gấp bội. Tỷ lệ khuếch đại phụ thuộc vào số máy tính trong mạng khuếch đại. Vì thế hacker chiếm được càng nhiều hệ thống mạng hoặc router cho phép chuyển trực tiếp các gói tin đến địa chỉ broadcast không qua chỗ lọc địa chỉ nguồn ở các đầu ra của gói tin thì cuộc tấn công càng dễ dàng hơn.

#### Cách chống Smurf flood

Cách đơn giản nhất để giải quyết tấn công với các hệ thống mạng này là tắt địa chỉa IP Broadcasting trên mỗi router/firewall trong hệ thống mạng đi. Việc này nhằm ngăn không cho router forward các gói tin ICMP đến các máy khác trong mạng. Các router mới hiện nay đều mặc định tắt địa chỉ IP Broadcasting nên hình thức tấn công này hiện nay không còn hiệu quả nữa. Tuy nhiên trên các hệ thống cũ chưa được nâng cấp, các hacker vẫn có thể lợi dụng để tấn công thông qua lỗ hổng này.

### Ping of death

#### Cách thức tấn công

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/ping-of-death.jpg)

Theo RFC 791 thì một gói tin IP có dung lượng tối đa là 65535 bytes. Tuy nhiên, lợi dụng việc gói tin sẽ được chia thành các gói tin nhỏ hơn tại tầng liên kết dữ liệu, kẻ tấn công có thể gửi gói tin với dung lượng lớn hơn 65535 bytes. Khi gói tin được kết hợp lại tại máy đích. Do dung lượng lớn hơn cho phép, dẫn đến không đủ dung lượng để chứa gói tin và máy đích bị crash.

#### Cách chống Ping of death 

Ta có thể kiểm tra kích thước gói tin trong lúc kết hợp các gói tin tại nơi nhận hoặc sử dụng bộ nhớ lớn hơn để xử lý gói tin. Tuy nhiên vào khoảng năm 1997-1998, lỗi nãy đã được fix, vì vậy bây giờ nó chỉ mang tính lịch sử.

### Teardrop

#### Cách thức tấn công

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/tear-drop.png)

Trong mạng chuyển mạch gói, dữ liệu được chia thành nhiều gói tin nhỏ, mỗi gói tin có một giá trị offset riêng và có thể truyền đi theo nhiều con đường khác nhau để tới đích. Tại đích, nhờ vào giá trị offset của từng gói tin mà dữ liệu lại được kết hợp lại như ban đầu.

Lợi dụng điều này, hacker có thể tạo ra nhiều gói tin có giá trị offset trùng lặp nhau hoặc xếp gối lên nhau gửi đến mục tiêu muốn tấn công.

Kết quả là máy tính đích không thể sắp xếp được những gói tin này và dẫn tới bị treo máy vì bị *“vắt kiệt”* khả năng xử lý.

### Cách chống Teardrop

Ta có thể ngăn chặn bằng cách kiểm tra offset và package length của gói tin, loại bỏ các gói tin có thứ tự không đúng trước khi sắp xếp các gói tin.

### SYN attack

#### Bắt tay ba bước trong kết nối TCP

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/three-way-handshake.jpg)

- Đầu tiên, máy tấn công gửi 1 packet tin SYN đến server để yêu cầu kết nối.
- Sau khi tiếp nhận packet SYN, server phản hồi lại client bằng một gói tin SYN/ACK, để xác nhận thông tin từ client.
- Client nhận được packet tin SYN/ACK thì sẽ trả lời server bằng gói tin ACK báo với server biết rằng nó đã nhận được packet tin SYN/ACK, kết nối đã được thiết lập và sẵn sàng trao đổi dữ liệu.

#### Cách thức tấn công 

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/syn-attack.jpg)

Lợi dụng trong quá trình bắt ta ba bước, ở bước 3 server phải đợi client gửi lại gói tin ACK hoặc hết thời gian timeout, kẻ tấn công thay vì gửi gói tin ACK như bình thường sẽ liên tục gửi các gói tin SYN đến server, server sẽ phản hồi lại từng kết nối nhưng vẫn dùng một phần tài nguyên để chờ tiếp nhận và phản hồi.

Kiểu tấn công này khiến cho server tốn tài nguyên cho các kết nối vô định. Khi lượng kết nối này đủ lớn sẽ khiến cho server không thể tiếp nhận thêm các kết nối khác.

#### Cách chống SYN attack

- Tăng số lượng kết nối tối đa của server: Cách này chỉ là giải pháp mang tính tạm thời do để tăng số lượng kết nối tối đa thì yêu cầu nhiều tài nguyên của server để giữ thêm các kết nối trong hàng đợi.
- SYN cookies: Server lưu lại tất cả những kết nối vào bảng hash với các thông số: IP, port, và những thông tin khác. Server chỉ cấp bộ nhớ cho kết nối khi nhận được gói tin thứ 3 của quá trình bắt tay 3 bước.
- Giảm thời gian SYN-RECEIVED
- RST cookies: khi nhận được gói tin SYN từ client, server cố tình gửi một gói tin không đúng với gói SYN /ACK mà client đang chờ đợi, thông thường client sẽ gửi lại server gói tin RST thông báo rằng nó không nhận được gói tin mong muốn và yêu cầu server gửi lại gói tin trước đó. Như vậy nếu nhận được phản hồi RST từ client thì client này vô hại và server bắt đầu thiết lập kết nối với client.

### UDP flood

#### Giao thức UDP

**UDP** hay User Datagram Protocol. **UDP** là một giao thức trên tầng mạng. Không giống như TCP/IP, UDP được sử dụng để gửi các gói tin ngắn gọi là datagram, cho phép truyền nhanh hơn nhưng không có cơ chế kiểm soát lỗi.

#### Cách thức tấn công

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/udp-flood.png)

Khi thực hiện phương thức tấn công này, tin tặc sẽ gửi một lượng lớn các gói tin UDP tới một số cổng ngẫu nhiên trên server. Máy chủ kiểm tra và trả lời với một **ICMP** **Destination Unreachable**. Khi số lượng yêu cầu UDP vượt quá ngưỡng cho phép, máy chủ sẽ mất khả năng xử lý request, dẫn đến tình trạng từ chối dịch vụ.

#### Cách chống UDP flood

Thông thường để chống lại UDP flood bằng cách chặn hoặc giới hạn số lượng UDP để ưu tiên tài nguyên cho các dịch vụ khác. Với các hệ thống tường lửa cấp thấp hoặc phần mềm tường lửa sẽ chỉ chịu được gần 1 triêu packet một giây (pps). Tuy nhiên khi số lượng packet vượt quá mức này hệ thống tường lửa sẽ quá tải.

### HTTP flood

#### Cách thức tấn công

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/http-flood-attack.png)

HTTP flood là cách tấn công gây quá tải bằng cách gửi hàng loạt yêu cầu GET hoặc POST hợp pháp đến máy chủ. Phương pháp này tuy tiêu tốn ít băng thông hơn các kiểu tấn công từ chối dịch vụ khác nhưng vẫn có thể buộc máy chủ sử dụng nguồn tài nguyên tối đa để xử lý tác vụ. Có 2 kiểu tấn công HTTP flood

- Sử dụng GET method: cách này thướng áp dụng với các server lưu trữ nhiều ảnh, tệp lớn
- Sử dụng POST method: cachs này sử dụng với các trang web, server có nhiều biểu mẫu, form.

#### Cách chống HTTP flood

Tuy HTTP flood sử dụng các request bình thường và khó nhận ra, tuy nhiên ta có thể dễ dàng phân biệt đâu là người dùng bình thường, đâu là bot bằng cách sử dụng Captcha.

### Slowloris

#### Cách thức tấn công

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/slowloris-attack-diagram.png)

Slowloris là một chương trình tấn công từ chối dịch vụ cho phép kẻ tấn công áp đảo server bằng cách mở và duy trì nhiều kết nối HTTP đồng thời giữa kẻ tấn công và mục tiêu.

- Attacker gửi các HTTP request không hoàn chỉnh đến server.
- Để duy trì và ngăn không cho server đóng kết nối, attacker sẽ gửi nhỏ giọt các phần của HTTP request.
- Server liên tục phải duy trì các kết nối, khi số lượng kết nối trở nên quá lớn, server sẽ quá tải.

#### Cách chống Slowloris

Để giảm thiểu ảnh hưởng do các cuộc tấn công Slowloris gây ra, ta có thể

- Tăng số lượng kết nối tối đa mà server có thể tiếp nhận.
- Giảm số lượng kết nối mà một địa chỉ IP có thể kết nối đến server.

### NTP amplification

#### Network time protocol (NTP)

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/ntp.png)

Đây là giao thức đồng bộ thời gian mạng. Mục đích của NTP là giúp cho các máy tính kết nối mạng luôn đồng bộ được giờ một cách chính xác. Các client gửi request đồng bộ giờ lên máy chủ, các máy chủ có thể có nhiều cấp sẽ cập nhật với nhau để đồng bộ chính xác giờ nhất cho client. Lớp cao nhất của hệ thống NTP là Stratum 0, thực chất là các đồng hồ nguyên tử có độ chính xác cực cao. Stratum 0 được kết nối bới các máy chủ Stratum 1. Các máy ở mức 1 sẽ tiếp tục cập nhật cho các máy mức 2 etc.

#### Cách thức tấn công

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/ntp-attack.jpg)

Attacker khai thác một lỗ hổng của giao thức NTP được ghi nhận có mã là CVE-2013-5211

Lỗ hổng lần này thực chất không hẳn là lỗ hổng mà là một “tính năng” của NTP. Tuy nhiên khi “tính năng” có phần hơi “cởi mở” này bị lợi dụng thì lại gây là hậu quả lớn. Đó là tính năng Monlist của NTP server, là 1 danh sách các máy tính đã kết nối tới NTP server. Khi nhận được một request yêu cầu cung cấp monlist, NTP server sẽ “vui vẻ” cung cấp danh sách các máy tính đã kết nối tới NTP server này mà không cần quan tâm xem ai là người đã request. Cứ có hỏi là “vui vẻ” trả lời. Ở đây chúng ta thấy ngay 1 vấn đề mà kẻ xấu đã lợi dụng để “khuếch đại”. Đó là 1 request nhỏ được gửi đi, server sẽ sinh ra 1 danh sách với kích thước lớn hơn rất nhiều so với request. Các request được gửi đi từ máy của hacker, nhưng đã làm giả source IP. Source IP sẽ bị sửa để trỏ đến địa chỉ IP của nạn nhân. Thế là các NTP server cứ thế trả các response về cho nạn nhân, trong khi máy này không hề gửi đi bất kỳ request nào. Đây giống một kiểu “ném đá giấu tay” kết hợp với “mượn gió bẻ măng”.

#### Cách chống NTP amplification 

Chúng ta cũng có thể cấu hình firewall để chặn hết các monlist request từ các địa chỉ IP bên ngoài mạng, để tránh bị lợi dụng

## Quá trình phát động một cuộc tấn công DDoS

Đầu tiên kẻ tấn công sẽ phát tán trojan horse vào nhiều máy tính khác nhau. Các máy tính này trở thành zombie *(máy tính bị chiếm quyền điều khiển)* và kết nối tới IRC server để nghe thêm nhiều lệnh sắp tới.

Server IRC có thể là một máy công cộng ở một trong các mạng IRC, nhưng cũng có thể là máy chuyên dụng do kẻ tấn công cài đặt lên một trong các máy bị chiếm quyền điều khiển.

Các bot chạy trên máy tính bị chiếm quyền điều khiển, hình thành một botnet.

Việc phát động tấn công DDoS có thể chia thành 4 giai đoạn

### Giai đoạn tạo botnet

Quá trình tạo botnet phụ thuộc phần lớn vào trình độ attacker, ở đây mình tạo một botnet đơn giản viết bằng python lây nhiễm khi người dùng vô tình cài đặt chương trình với quyền **sudo**

Dưới đây là hình ảnh một máy đã bị lây nhiễm, bot sẽ được khởi chạy khi bật máy và sẵn sàng nhận lệnh attacker.

### Giai đoạn cấu hình 

Đây là giai đoạn cung cấp server IRC và kênh thông tin. Sau khi cài đặt lên một máy tính đã được kiểm soát, bot sẽ kết nối tới host được chọn. Đầu tiên kẻ tấn công nhập dữ liệu cần thiết vào để giới hạn quyền truy cập bot, bảo vệ an toàn cho kênh và cuối cùng cung cấp một danh sách người dùng được cấp phép *(những người có thể điều khiển bot)*. Ở giai đoạn này, bot có thể được điều chỉnh sâu hơn, như định nghĩa phương thức tấn công và đích đến.

Ở đây mình chọn server irc là [freenode](https://webchat.freenode.net/) để làm server điều khiển các bot.

### Giai đoạn điều khiển

Đây là giai đoạn gồm một số hoạt động thực hiện sau khi bot đã được cài đặt lên máy đích trong một thư mục chọn. Để bot khởi động với linux ta ùng lệnh `sudo systemctl enable bot`

Việc đầu tiên bot thực hiện sau khi được cài đặt thành công là kết nối tới một server IRC và liên kết với kênh điều khiển thông qua sử dụng một mật khẩu. Nickname trên IRC được tạo ngẫu nhiên. Sau đó, bot ở trạng thái sẵn sàng chờ lệnh từ ứng dụng chủ. Kẻ tấn công cũng phải sử dụng một mật khẩu để kết nối tới botnet. Điều này là cần thiết để không ai khác có thể sử dụng mạng botnet đã được cung cấp.

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/config.png)

IRC không chỉ cung cấp phương tiện điều khiển hàng trăm bot mà còn cho phép kẻ tấn công sử dụng nhiều kỹ thuật khác nhau để ẩn nhân dạng thực của chúng. Điều đó khiến việc đối phó trước các cuộc tấn công trở nên khó khăn. Nhưng may mắn là, do đặc điểm tự nhiên của chúng, các botnet luôn tạo ra lưu lượng đáng ngờ, tạo điều kiện dễ dàng để có thể dò tìm nhờ một số kiểu mẫu hay mô hình đã biết. Điều đó giúp các quản trị viên IRC phát hiện và can thiệp kịp thời, cho phép họ gỡ bỏ các mạng botnet và những sự lạm dụng không đáng có trên hệ thống của họ.

Trước tình hình này, những kẻ tấn công buộc phải nghĩ ra cách thức khác, cải tiến kỹ thuật C&C *(Control and Command - Điều khiển qua lệnh)* thành botnet hardening. Ở kỹ thuật mới này, các bot thường được cấu hình để kết nối với nhiều server khác nhau, sử dụng một hostname ánh xạ động. Nhờ đó, kẻ tấn công có thể chuyển bot sang server mới dễ dàng, vẫn hoàn toàn nắm quyền kiểm soát ngay cả khi bot đã bị phát hiện. Các dịch vụ DNS động như dyndns.com hay no-IP.com thường được dùng trong kiểu tấn công này.

Một DNS động *(như RFC 2136)* là một hệ thống liên kết tên miền với địa chỉ IP động. Người dùng kết nối Internet qua modem, ADSL hoặc cáp thường không có địa chỉ IP cố định. Khi một đối tượng người dùng kết nối tới Internet, nhà cung cấp dịch vụ mạng (ISP) sẽ gán một địa chỉ IP chưa được sử dụng lấy ra từ vùng được chọn. Địa chỉ này thường được giữ nguyên cho tới khi người dùng ngừng sử dụng kết nối đó.

Cơ chế này giúp các hãng cung cấp dịch vụ mạng (ISP) tận dụng được tối đa khả năng khai thác địa chỉ IP, nhưng cản trở đối tượng người dùng cần thực hiện một số dịch vụ nào đó qua mạng Internet trong thời gian dài, song không phải sử dụng địa chỉ IP tĩnh. Để giải quyết vấn đề này, DNS động được cho ra đời. Hãng cung cấp sẽ tạo cho dịch vụ một chương trình chuyên dụng, gửi tín hiệu tới cơ sở dữ liệu DNS mỗi khi địa chỉ IP của người dùng thay đổi.

Để ẩn hoạt động, kênh IRC được cấu hình giới hạn quyền truy cập và ẩn thao tác. Các mô hình IRC điển hình cho kênh botnet là:

- k *(đòi hỏi phải nhập mật khẩu khi dùng kênh)*
- s *(không được hiển thị trên danh sách các kênh công cộng)*
- u *(chỉ có người điều hành operator* là được hiển thị trên danh sách người dùng);
- m (*chỉ có người dùng ở trạng thái sử dụng âm thanh +v mới có thể gửi tin đến kênh)*.

Hầu hết kẻ tấn công đều dùng server IRC cá nhân, mã hoá tất cả liên lạc trên kênh dẫn. Chúng cũng có khuynh hướng sử dụng nhiều biến thể cá nhân hoá của phần mềm IRC server, được cấu hình để nghe trên các cổng ngoài tiêu chuẩn và sử dụng phiên bản đã được chỉnh sửa của giao thức, để một IRC client thông thường không thể kết nối vào mạng.

### Giai đoạn tấn công

Trong giai đoạn này có thể áp dụng nhiều phương pháp tấn công với nhau để đạt hiệu quả cao nhất, ở đây để đơn giảm mình sử dụng ping flood attack

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/attack-freenode.png)

Ở máy bị tấn công ta thấy trong phần network tăng lên bất thường.

![](https://raw.githubusercontent.com/danghh-1998/ddos_attack/master/images/attack.png)

## Cách phòng chống DDoS

DDoS không thể ngăn chặn hoàn toàn, tuy nhiên ta vẫn có những phương pháp để phòng chống nhằm giảm thiểu thiệt hại do DDoS gây ra.

Có rất nhiều giải pháp và ý tưởng được đưa ra nhằm đối phó với các cuộc tấn công kiểu DDoS. Tuy nhiên không có giải pháp và ý tưởng nào là giải quyết trọn vẹn bài toán Anti-DDoS. Các hình thái khác nhau của DDoS liên tục xuất hiện theo thời gian song song với các giải pháp đối phó, tuy nhiên cuộc đua vẫn tuân theo quy luật tất yếu của bảo mật máy tính: *“Hacker luôn đi trước giới bảo mật một bước”*.

**Có ba giai đoạn chính trong quá trình Anti-DDoS:**

- Giai đoạn ngăn ngừa: tối thiểu hóa lượng Agent, tìm và vô hiệu hóa các Handler

- Giai đoạn đối đầu với cuộc tấn công: Phát hiện và ngăn chặn cuộc tấn công, làm suy giảm và dừng cuộc tấn công, chuyển hướng cuộc tấn công.

- Giai đoạn sau khi cuộc tấn công xảy ra: thu thập chứng cứ và rút kinh nghiệm

Các giai đoạn chi tiết trong phòng chống DDoS được liệt kê sau đây

### Tối thiểu hóa số lượng Agent

- Từ phía User: một phương pháp rất tốt để năng ngừa tấn công DDoS là từng internet user sẽ tự đề phòng không để bị lợi dụng tấn công hệ thống khác. Muốn đạt được điều này thì ý thức và kỹ thuật phòng chống phải được phổ biến rộng rãi cho các internet user. Attack-Network sẽ không bao giờ hình thành nếu không có user nào bị lợi dụng trở thành Agent. Các user phải liên tục thực hiện các quá trình bảo mật trên máy vi tính của mình. Họ phải tự kiểm tra sự hiện diện của Agent trên máy của mình, điều này là rất khó khăn đối với user thông thường.
- Một số giải pháp tích hợp sẵn khả năng ngăn ngừa việc cài đặt code nguy hiểm vào phần cứng và phần mềm của từng hệ thống. Về phía user họ nên cài đặt và update liên tục các software như antivirus, anti trojan và server patch của hệ điều hành.
- Từ phía Network Service Provider: Thay đổi cách tính tiền dịch vụ truy cập theo dung lượng sẽ làm cho user lưu ý đến những gì họ gửi, như vậy về mặt ý thức tăng cường phát hiện DDoS Agent sẽ tự nâng cao ở mỗi User.

### Tìm và vô hiệu hóa các Handler

Một nhân tố vô cùng quan trọng trong attack-network là Handler, nếu có thể phát hiện và vô hiệu hóa Handler thì khả năng Anti-DDoS thành công là rất cao. Bằng cách theo dõi các giao tiếp giữa Handler và Client hay handler va Agent ta có thể phát hiện ra vị trí của Handler. Do một Handler quản lý nhiều agent, nên triệt tiêu được một Handler cũng có nghĩa là loại bỏ một lượng đáng kể các Agent trong Attack – Network.

## Nhận biết tấn công DDoS

Tấn công Dos/DDos đôi khi rất khó để phân biệt với các hoạt động truy cập mạng thông thường. Tuy nhiên có nhiều kỹ thuật có thể phát hiện các cuộc tấn công DDoS

### Agress Filtering

Kỹ thuật này kiểm tra xem một packet có đủ tiêu chuẩn ra khỏi một subnet hay không dựa trên cơ sở gateway của một subnet luôn biết được địa chỉ IP của các máy thuộc subnet.

Các packet từ bên trong subnet gửi ra ngoài với địa chỉ nguồn không hợp lệ sẽ bị giữ lại để điều tra nguyên nhân. Nếu kỹ thuật này được áp dụng trên tất cả các subnet của internet thì khái niệm giả mạo địa chỉ IP sẽ không còn tồn tại.

### MIB statistics

Trong Management Information Base (SNMP) của route luôn có thông tin thống kể về sự biến thiên trạng thái của mạng. Nếu ta giám sát chặt chẽ các thống kê của Protocol ICMP, UDP và TCP ta sẽ có khả năng phát hiện được thời điểm bắt đầu của cuộc tấn công để tạo *“quỹ thời gian vàng”* cho việc xử lý tình huống.

## Làm suy giảm các cuộc tấn công

### Load balancing

Thiết lập kiến trúc cân bằng tải cho các server trọng điểm sẽ làm gia tăng thời gian chống chọi của hệ thống với cuộc tấn công DDoS. Tuy nhiên, điều này không có ý nghĩa lắm về mặt thực tiễn vì quy mô của cuộc tấn công là không có giới hạn.

### Throttling

Thiết lập cơ chế điều tiết trên router, quy định một khoảng tải hợp lý mà server bên trong có thể xử lý được. Phương pháp này cũng có thể được dùng để ngăn chặn khả năng DDoS traffic không cho user truy cập dịch vụ. Hạn chế của kỹ thuật này là không phân biệt được giữa các loại traffic, đôi khi làm dịch vụ bị gián đoạn với user, DDoS traffic vẫn có thể xâm nhập vào mạng dịch vụ nhưng với số lượng hữu hạn.

### Drop request

Thiết lập cơ chế drop request nếu nó vi phạm một số quy định như: thời gian delay kéo dài, tốn nhiều tài nguyên để xử lý, gây deadlock. Kỹ thuật này triệt tiêu khả năng làm cạn kiệt năng lực hệ thống, tuy nhiên nó cũng giới hạn một số hoạt động thông thường của hệ thống, cần cân nhắc khi sử dụng.

## Chuyển hướng các cuộc tấn công

### Honeyspots

Một kỹ thuật đang được nghiên cứu là Honeyspots. Honeyspots là một hệ thống được thiết kế nhằm đánh lừa attacker tấn công vào khi xâm nhập hệ thống mà không chú ý đến hệ thống quan trọng thực sự.

Honeyspots không chỉ đóng vai trò *“Lê Lai cứu chúa”* mà còn rất hiệu quả trong việc phát hiện và xử lý xâm nhập, vì trên Honeyspots đã thiết lập sẵn các cơ chế giám sát và báo động.

Ngoài ra Honeyspots còn có giá trị trong việc học hỏi và rút kinh nghiệm từ attacker, do Honeyspots ghi nhận khá chi tiết mọi động thái của attacker trên hệ thống. Nếu attacker bị đánh lừa và cài đặt Agent hay Handler lên Honeyspots thì khả năng bị triệt tiêu toàn bộ attack-network là rất cao.

## Truy vết sau tấn công

### Traffic Pattern Analysis

Nếu dữ liệu về thống kê biến thiên lượng traffic theo thời gian đã được lưu lại thì sẽ được đưa ra phân tích. Quá trình phân tích này rất có ích cho việc tinh chỉnh lại các hệ thống Load Balancing và Throttling. Ngoài ra các dữ liệu này còn giúp Quản trị mạng điều chỉnh lại các quy tắc kiểm soát traffic ra vào mạng của mình.

### Packet Traceback

Bằng cách dùng kỹ thuật Traceback ta có thể truy ngược lại vị trí của attacker *(ít nhất là subnet của attacker)*. Từ kỹ thuật Traceback ta phát triển thêm khả năng Block Traceback từ attacker khá hữu hiệu. gần đây đã có một kỹ thuật Traceback khá hiệu quả có thể truy tìm nguồn gốc của cuộc tấn công dưới 15 phút.