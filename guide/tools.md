# 查詢工具（免金鑰優先）

> 給 AI：你能上網或能執行程式時，優先用這些官方、免費的資料來源，結果附上來源與查詢時間。
> 不能上網時，告訴使用者去哪裡查、查什麼。以下為 2026-10 的狀態（🔄 服務會變，失效就換）。

## 天氣

- **Open-Meteo**（`https://api.open-meteo.com/v1/forecast?latitude=..&longitude=..&hourly=temperature_2m,apparent_temperature,wind_speed_10m,wind_gusts_10m,precipitation,cloud_cover_low`）：
  全球逐時預報，免金鑰；另有 archive API 可查過去的逐時天氣（寫檢討用）。
- **met.no Locationforecast 2.0**（`https://api.met.no/weatherapi/locationforecast/2.0/complete?lat=..&lon=..`，要帶 User-Agent）：
  北歐最準；前約 48 小時逐時，之後每 6 小時。
- 判讀：山上陣風 × 1.5、毛毛雨到山上要穿雨衣（`guide/baselines.md`）。
- 日本：日本氣象廳（JMA）預報；**櫻花、紅葉預測**看日本氣象協會 tenki.jp 或 Weathernews（🔄 預測通常在季節前 1–3 個月公布、會更新多次）。
- 極光：NOAA 3 天 Kp 指數預報＋當地雲量＋天夠不夠黑。經驗上高緯度（約北緯 68°）Kp 不高也有機會，越往南需要越高；只能說「有機會」，不保證看得到。

## 大眾運輸與班次

| 地區 | 查法 |
|---|---|
| 挪威（渡輪、公車、火車） | **Entur** API：geocoder `https://api.entur.io/geocoder/v1/autocomplete?text=<站名>` 取站點 id → journey-planner GraphQL（header `ET-Client-Name`）。==當天出發前再查即時資訊==，官網 PDF 可能過期 |
| 瑞典斯德哥爾摩 SL | `journeyplanner.integration.sl.se` 行程規劃；`transport.integration.sl.se/v1/sites/<id>/departures` 即時到站 |
| 荷蘭 | 9292.nl（全交通方式）、NS app（火車）；可直接感應信用卡或手機進出站 |
| 韓國 | 地圖用 Naver Map 或 KakaoMap（Google Maps 在韓國的步行與開車導航不完整 🔄）；交通卡 T-money 或觀光用卡（🔄） |
| 日本 | 換乘查詢：Jorudan、NAVITIME、Google Maps；JR 各公司官網（JR 東日本、JR 西日本、JR 九州…）的周遊券與網路訂票；高速巴士比價網站 |
| 歐洲長途巴士 | FlixBus（便宜、常誤點 1–2 小時，不要接太緊的行程）、Rome2Rio（看有哪些交通方式） |
| 道路狀況 | 各國公路主管機關網站（例：挪威 vegvesen.no、瑞典 trafikverket.se） |

很多城市的大眾運輸可以直接感應信用卡或手機（不用買票卡）；先查，再算一日券划不划算。機場巴士常不在都市票系統內。

## 路線與地圖

==先查目的地主流的地圖 app==：有些國家（例：韓國、中國）Google Maps 導航不完整，要改用當地 app（🔄）。叫車 app 也依國家不同（例：東南亞 Grab）。

- **OSRM**（`router.project-osrm.org`）開車路線；`routing.openstreetmap.de` 有步行、腳踏車版本。
  ==檢查結果裡有沒有渡輪段==：曾經把 41 公里的渡輪算成公路。
- **Google Maps 多點路線連結**：`https://www.google.com/maps/dir/?api=1&origin=..&destination=..&waypoints=a|b|c`
  （手機版約只吃 3 個中途點，太多就拆段；起點用「目前位置」）。
- 離線：Google Maps 離線區域、HERE WeGo、Organic Maps。

## 機場與航班

- 座位圖：aeroLOPA。
- 入境規定：IATA Travel Centre、各國官方網站、外交部領事事務局。
- 機場配置：機場官網的航廈地圖（看安檢與護照查驗的位置、過關後有沒有餐廳、貴賓室在哪一區）。

## 回顧與紀錄

- **照片的拍攝時間與位置（EXIF）是最準的時間紀錄**：回來寫檢討時，用照片推每個點幾點到、停多久。
  照片含精確位置與時間：共享相簿只給同行者；公開分享前移除位置資訊。
  前提是同行者當天就上傳照片到共享相簿。
- 手機定位紀錄（Google 時間軸等）：位置大致可信，時間可能晚十幾二十分鐘，只看大概。
- 優先順序：**本人記得的 ＞ 照片 ＞ 定位**。

## 其他好用的

- 規劃資訊：背包客棧、PTT（各國旅遊板）、部落格、YouTube 遊記。
- 機票：Google Flights、Skyscanner。
- 語音導覽：把查證過的導覽稿用文字轉語音工具（例：Microsoft Edge 的朗讀語音）轉成音檔，開車或逛博物館時聽。
- 回台灣可以帶什麼：財政部關務署的入境旅客須知。

## 給會寫程式的使用者

這些查詢都可以寫成小程式，讓 AI 每天自動跑：例如每天傍晚查極光機會並推播到手機、在免費取消期限前查天氣給建議。
用 Claude Code／Codex 的話，可以請 AI 直接幫你寫。
