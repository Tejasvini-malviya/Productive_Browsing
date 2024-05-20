chrome.webNavigation.onCompleted.addListener(function(details) {
  chrome.storage.sync.get(['restrictedSites', 'timeLimits'], function(data) {
      const restrictedSites = data.restrictedSites || [];
      const timeLimits = data.timeLimits || [];

      const url = new URL(details.url);
      const hostname = url.hostname;

      if (restrictedSites.includes(hostname)) {
          chrome.tabs.remove(details.tabId);
          alert('This site is restricted!');
      } else {
          const timeLimit = timeLimits.find(limit => limit.url === hostname);
          if (timeLimit) {
              // Handle time limit logic here
          }
      }
  });
});
