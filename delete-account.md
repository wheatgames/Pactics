---
layout: "document"
title: "Delete your account"
description: "How to request deletion of your Pactics account and account-linked data."
nav_key: "delete-account"
permalink: "/delete-account.html"
request_subject: "Delete my Pactics account"
---

# Delete your Pactics account

**Pactics** is developed by **Yufen Quan** (WheatGames Studio on Google Play). This page explains how to delete your Pactics account and the data linked to it.

## How to request deletion

You can request deletion in either of these ways. **You do not need to reinstall the Game to make a request.**

1. **In the Game:** open **Settings > Manage Account > Delete Account** and confirm.
2. **By email:** send a message to **wheatgames123@gmail.com** with the subject "Delete my Pactics account".

### What to include in your email

Creating a Pactics account does not require your real name, email address or phone number; accounts are identified by a Player ID. To help us find your account, please include **at least one** of the following:

- **Your Player ID**, if you still have it. It is shown on your **Player Profile** screen in the Game.
- **The order number of any in-app purchase you made in Pactics.** You can find it in the purchase receipt email from Apple or Google, at [reportaproblem.apple.com](https://reportaproblem.apple.com/) (App Store) or in your [Google Play order history](https://play.google.com/store/account/orderhistory). An order number can help us find the account linked to that purchase.

If possible, also tell us your platform (iOS or Android), your device model and the approximate date you started playing.

### If you do not have a Player ID or an order number

You can still send us a deletion request. We will search our records with the information you give us and reply to tell you whether we could find and delete your account.

If we cannot identify your account, the reason is usually that the account is not linked to any information that can identify you.

- **If your account was linked to Game Center (iOS) or Google Play Games (Android):** you can also install the Game, sign in with the same platform account to restore it, and then delete it yourself with **Settings > Manage Account > Delete Account**. This is an optional extra route, not a requirement for making a request.
- **If you only played as a guest:** reinstalling the Game may create a new guest account instead of restoring the old one (for example, on iOS after all apps from the same developer have been removed from the device). In that case we may not be able to find or restore the old guest account.

### Verification

A Player ID or order number helps us find an account, but on its own it does not prove that the account is yours. Before deleting, we take reasonable steps to confirm that you are the owner, for example by asking you to confirm details that only the owner is likely to know (such as the item, date and price of a purchase, or your platform and device). If we cannot reasonably confirm ownership, we will tell you and will not delete the account. We will never ask for your password, payment card details or any government ID.

We will confirm your request and complete the deletion within **30 days** after we have identified your account.

## What is deleted

We delete the data linked to your account in our own systems, and we ask the service providers that store this data for us to delete it as well:

- Your player account and player IDs (Microsoft PlayFab and Google Firebase Authentication).
- Your nickname, cloud save and game progress (Microsoft PlayFab and Google Cloud Firestore).
- Your customer record and the link between your account and your purchase history in our purchase service (RevenueCat), except for transaction records we must keep as described below.

## What may be kept

- Purchase transaction records that we are required to keep for legal, tax or accounting reasons.
- Data held by Apple or Google for purchases you made through their stores, which is governed by their own policies.
- Aggregated or anonymized statistics that can no longer identify you.
- Analytics and crash reports (Google Firebase) and advertising data (Appodeal and its advertising partners). We do not link this data to your Player ID or account, so it cannot be looked up or deleted by account; it is tied to app-instance or device identifiers. Its retention and deletion are governed by these providers' privacy policies and applicable law. You can reset your device's advertising identifier at any time in your device settings.
- Emails you sent us, which are kept as described in our [Privacy Policy]({{ '/privacy.html' | relative_url }}).

Deleting your account cannot be undone. Purchased items and progress cannot be restored afterwards.

See our full [Privacy Policy]({{ '/privacy.html' | relative_url }}) for more details.
