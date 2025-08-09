import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.yourname.sieutool',
  appName: 'Sieu Tool AI',
  webDir: '.',
  bundledWebRuntime: false,
  server: {
    allowNavigation: [
      'i.ibb.co',
      'upload.wikimedia.org',
      'placehold.co',
      'cdnjs.cloudflare.com',
      'fonts.googleapis.com',
      'fonts.gstatic.com',
      'www.youtube.com',
      'i.ytimg.com'
    ]
  },
  plugins: {
    SplashScreen: {
      launchShowDuration: 0
    }
  }
};

export default config;