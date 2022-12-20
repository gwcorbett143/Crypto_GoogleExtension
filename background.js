//this file sets up the popup so when I click the icon it shows up

let color = "#3AA757";

chrome.runtime.onInstalled.addListener(() =>{
	chrome.storage.sync.set({color});
	console.log('Default background color set to ${color}');
});