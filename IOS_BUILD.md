# iOS Build (Capacitor)

## 1) Cài đặt
```bash
npm i @capacitor/core @capacitor/cli -D
```

## 2) Khởi tạo & đồng bộ
```bash
npm run cap:init
npm run cap:add:ios
npm run cap:sync
npm run cap:open:ios
```

## 3) Mở Xcode (sau `npm run cap:open:ios`)
- Chọn Team signing, Bundle ID (com.yourname.sieutool -> đổi tên bạn).
- Trong `AppDelegate.swift` (hoặc nơi cấu hình WKWebView), bật phát media inline:
  ```swift
  import Capacitor
  // ...
  (bridge?.webView?.configuration).allowsInlineMediaPlayback = true
  if #available(iOS 10.0, *) {
      (bridge?.webView?.configuration).mediaTypesRequiringUserActionForPlayback = []
  }
  ```
- Tạo icon/splash:
  ```bash
  npx @capacitor/assets generate
  ```

## 4) Build & chạy
- Chọn thiết bị thật → `Product > Run` trong Xcode.

## 5) Lên App Store
- `Product > Archive` → Distribute (TestFlight) → Submit for Review.

## Ghi chú
- `capacitor.config.ts` đã whiltelist các domain bạn dùng (fonts, cdnjs, youtube, ibb, wiki, placehold).
- Service Worker chỉ đăng ký khi chạy trên web (không đăng ký trong app native).
- Nếu bạn đã build Tailwind CSS (`tailwind.css`), nên thay CDN bằng `<link rel="stylesheet" href="tailwind.css">` trước khi đóng gói.