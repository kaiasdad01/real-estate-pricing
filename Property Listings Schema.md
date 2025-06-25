Property Listings Schema

This page contains a data dictionary and a description of all response fields for our property sale listings and rental listings endpoints (`/listings`).

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Property Listings Response Fields

The following response fields will be returned as part of both sale and rental listing records:

<Table align={["left","left","left"]}>
  <thead>
    <tr>
      <th>
        Response Field
      </th>

      <th>
        Description
      </th>

      <th>
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `id`
      </td>

      <td>
        Property Id\
        *Data type: String*  

        A unique RentCast property identifier
      </td>

      <td>
        `"3821-Hargis-St,-Austin,-TX-78723"`
      </td>
    </tr>

    <tr>
      <td>
        `formattedAddress`
      </td>

      <td>
        Formatted Address\
        *Data type: String*  

        The full property address, in the format `Street, Unit, City, State Zip`
      </td>

      <td>
        `"3821 Hargis St, Austin, TX 78723"`
      </td>
    </tr>

    <tr>
      <td>
        `addressLine1`
      </td>

      <td>
        Address Line 1\
        *Data type: String*  

        The first line of the property street address
      </td>

      <td>
        `"3821 Hargis St"`
      </td>
    </tr>

    <tr>
      <td>
        `addressLine2`
      </td>

      <td>
        Address Line 2\
        *Data type: String*  

        The second line of the property street address, typically containing the unit or apartment identifier
      </td>

      <td>
        `"Apt 12"`
      </td>
    </tr>

    <tr>
      <td>
        `city`
      </td>

      <td>
        Address City\
        *Data type: String*  

        The city of the property address
      </td>

      <td>
        `"Austin"`
      </td>
    </tr>

    <tr>
      <td>
        `state`
      </td>

      <td>
        Address State\
        *Data type: String*  

        The state of the property address, as a 2-character abbreviation
      </td>

      <td>
        `"TX"`
      </td>
    </tr>

    <tr>
      <td>
        `zipCode`
      </td>

      <td>
        Address Zip Code\
        *Data type: String*  

        The 5-digit zip code of the property address
      </td>

      <td>
        `"78723"`
      </td>
    </tr>

    <tr>
      <td>
        `county`
      </td>

      <td>
        County\
        *Data type: String*  

        The county in which the property is located
      </td>

      <td>
        `"Travis"`
      </td>
    </tr>

    <tr>
      <td>
        `latitude`
      </td>

      <td>
        Latitude\
        *Data type: Number*  

        The latitude of the property's geographical location
      </td>

      <td>
        `30.290643`
      </td>
    </tr>

    <tr>
      <td>
        `longitude`
      </td>

      <td>
        Longitude\
        *Data type: Number*  

        The longitude of the property's geographical location
      </td>

      <td>
        `-97.701547`
      </td>
    </tr>

    <tr>
      <td>
        `propertyType`
      </td>

      <td>
        Property Type\
        *Data type: String (Enum)*  

        The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) for possible values
      </td>

      <td>
        `"Single Family"`
      </td>
    </tr>

    <tr>
      <td>
        `bedrooms`
      </td>

      <td>
        Number of Bedrooms\
        *Data type: Number*  

        The number of bedrooms in the property, with a value of "0" indicating a studio layout
      </td>

      <td>
        `4`
      </td>
    </tr>

    <tr>
      <td>
        `bathrooms`
      </td>

      <td>
        Number of Bathrooms\
        *Data type: Number*  

        The number of bathrooms in the property
      </td>

      <td>
        `2.5`
      </td>
    </tr>

    <tr>
      <td>
        `squareFootage`
      </td>

      <td>
        Living Area (Sq.Ft.)\
        *Data type: Number*  

        The total indoor living area of the property, in square feet
      </td>

      <td>
        `2345`
      </td>
    </tr>

    <tr>
      <td>
        `lotSize`
      </td>

      <td>
        Lot Area (Sq.Ft.)\
        *Data type: Number*  

        The total lot size of the property parcel, in square feet
      </td>

      <td>
        `3284`
      </td>
    </tr>

    <tr>
      <td>
        `yearBuilt`
      </td>

      <td>
        Year Built\
        *Data type: Number*  

        The year in which the property was constructed
      </td>

      <td>
        `2008`
      </td>
    </tr>

    <tr>
      <td>
        `hoa`
      </td>

      <td>
        HOA Details\
        *Data type: Object*  

        Information about the property's homeowner's association (HOA)
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        `hoa.fee`
      </td>

      <td>
        HOA Fee Amount (Monthly)\
        *Data type: Number*  

        The total monthly HOA fee or assessment amount
      </td>

      <td>
        `65`
      </td>
    </tr>

    <tr>
      <td>
        `status`
      </td>

      <td>
        Listing Status\
        *Data type: String (Enum)*  

        The current property listing status. See [explanation of listing statuses](#listing-status-field-values) for possible values
      </td>

      <td>
        `"Active"`
      </td>
    </tr>

    <tr>
      <td>
        `price`
      </td>

      <td>
        Listed Price or Rent\
        *Data type: Number*  

        The listed price or rent of the property listing
      </td>

      <td>
        `899000`
      </td>
    </tr>

    <tr>
      <td>
        `listingType`
      </td>

      <td>
        Listing Type\
        *Data type: String (Enum)*  

        The type of the property listing. See [explanation of listing types](#listing-type-field-values) for possible values
      </td>

      <td>
        `"Standard"`
      </td>
    </tr>

    <tr>
      <td>
        `listedDate`
      </td>

      <td>
        Date Listed\
        *Data type: Date*  

        The date the property was most recently listed for sale or rent, in ISO 8601 format
      </td>

      <td>
        `"2024-06-24T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        `removedDate`
      </td>

      <td>
        Date Delisted\
        *Data type: Date*  

        The date the property listing was most recently removed or delisted, in ISO 8601 format
      </td>

      <td>
        `"2024-10-01T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        `createdDate`
      </td>

      <td>
        Date Created\
        *Data type: Date*  

        The date the property listing was first seen and created, in ISO 8601 format
      </td>

      <td>
        `"2021-06-25T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        `lastSeenDate`
      </td>

      <td>
        Date Last Seen\
        *Data type: Date*  

        The date the property listing was most recently seen as active, in ISO 8601 format
      </td>

      <td>
        `"2024-09-30T13:11:47.157Z"`
      </td>
    </tr>

    <tr>
      <td>
        `daysOnMarket`
      </td>

      <td>
        Days on Market\
        *Data type: Number*  

        The number of days the property listing has been active
      </td>

      <td>
        `99`
      </td>
    </tr>

    <tr>
      <td>
        `mlsName`
      </td>

      <td>
        MLS Name\
        *Data type: String*  

        The MLS name of the property listing, if listed on the Multiple Listing Service (MLS)
      </td>

      <td>
        `"UnlockMLS"`
      </td>
    </tr>

    <tr>
      <td>
        `mlsNumber`
      </td>

      <td>
        MLS Number\
        *Data type: String*  

        The MLS number or unique identifier of the property listing, if listed on the Multiple Listing Service (MLS) 
      </td>

      <td>
        `"5519228"`
      </td>
    </tr>

    <tr>
      <td>
        `listingAgent`
      </td>

      <td>
        Listing Agent Details\
        *Data type: Object*  

        Information about the listing agent of the property, typically representing the property seller
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        `listingAgent.name`
      </td>

      <td>
        Listing Agent - Name\
        *Data type: String*  

        The name of the listing agent, typically in the format `First Last`
      </td>

      <td>
        `"Jennifer Welch"`
      </td>
    </tr>

    <tr>
      <td>
        `listingAgent.phone`
      </td>

      <td>
        Listing Agent - Phone Number\
        *Data type: String*  

        The phone number of the listing agent, typically consisting of 10 digits, including the area code
      </td>

      <td>
        `"5124313110"`
      </td>
    </tr>

    <tr>
      <td>
        `listingAgent.email`
      </td>

      <td>
        Listing Agent - Email Address\
        *Data type: String*  

        The email address of the listing agent
      </td>

      <td>
        `"jennifer@example.com"`
      </td>
    </tr>

    <tr>
      <td>
        `listingAgent.website`
      </td>

      <td>
        Listing Agent - Website URL\
        *Data type: String*  

        The website URL of the listing agent
      </td>

      <td>
        `"https://example.com"`
      </td>
    </tr>

    <tr>
      <td>
        `listingOffice`
      </td>

      <td>
        Listing Office Details\
        *Data type: Object*  

        Information about the listing office or broker of the property, typically representing the property seller
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        `listingOffice.name`
      </td>

      <td>
        Listing Office - Name\
        *Data type: String*  

        The name of the listing office or broker
      </td>

      <td>
        `"Gottesman Residential RE"`
      </td>
    </tr>

    <tr>
      <td>
        `listingOffice.phone`
      </td>

      <td>
        Listing Office - Phone Number\
        *Data type: String*  

        The phone number of the listing office or broker, typically consisting of 10 digits, including the area code
      </td>

      <td>
        `"5124512422"`
      </td>
    </tr>

    <tr>
      <td>
        `listingOffice.email`
      </td>

      <td>
        Listing Office - Email Address\
        *Data type: String*  

        The email address of the listing office or broker
      </td>

      <td>
        `"jennifer@example.com"`
      </td>
    </tr>

    <tr>
      <td>
        `listingOffice.website`
      </td>

      <td>
        Listing Office - Website URL\
        *Data type: String*  

        The website URL of the listing office or broker
      </td>

      <td>
        `"https://example.com"`
      </td>
    </tr>

    <tr>
      <td>
        `builder`
      </td>

      <td>
        Builder Details\
        *Data type: Object*  

        Information about the builder of the property. This field will only be present for new construction listings
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        `builder.name`
      </td>

      <td>
        Builder - Name\
        *Data type: String*  

        The name of the property builder
      </td>

      <td>
        `"Pulte Homes"`
      </td>
    </tr>

    <tr>
      <td>
        `builder.development`
      </td>

      <td>
        Builder - Development Name\
        *Data type: String*  

        The name of the development or new construction community in which the property is located
      </td>

      <td>
        `"Hampton Lakes at River Hall"`
      </td>
    </tr>

    <tr>
      <td>
        `builder.phone`
      </td>

      <td>
        Builder - Phone Number\
        *Data type: String*  

        The phone number of the property builder, typically consisting of 10 digits, including the area code
      </td>

      <td>
        `"2392300326"`
      </td>
    </tr>

    <tr>
      <td>
        `builder.website`
      </td>

      <td>
        Builder - Website URL\
        *Data type: String*  

        The website URL of the property builder
      </td>

      <td>
        `"https://example.com"`
      </td>
    </tr>

    <tr>
      <td>
        `history`
      </td>

      <td>
        Listing History\
        *Data type: Object*  

        A list of historical listing entries for this property, with JSON keys indicating the listing date, in the format `YYYY-MM-DD`
      </td>

      <td>
        `{ "2024-06-24": { ... } }`
      </td>
    </tr>

    <tr>
      <td>
        `history[YYYY-MM-DD]`
      </td>

      <td>
        Listing History Entry\
        *Data type: Object*  

        A single historical listing entry, with listing information specific to a past listing date
      </td>

      <td>
        `{ ... }`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .event
        ```
      </td>

      <td>
        Listing History Entry - Event Type\
        *Data type: String (Enum)*  

        The type of the historical listing entry, with possible values of "Sale Listing" for sale listings, or "Rental Listing" for rental listings
      </td>

      <td>
        `"Sale Listing"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .price
        ```
      </td>

      <td>
        Listing History Entry - Listed Price or Rent\
        *Data type: Number*  

        The last known listed price or rent of the property listing
      </td>

      <td>
        `899000`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .listingType
        ```
      </td>

      <td>
        Listing History Entry - Listing Type\
        *Data type: String (Enum)*  

        The type of the property listing. See [explanation of listing types](#listing-type-field-values)  for possible values
      </td>

      <td>
        `"Standard"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .listedDate
        ```
      </td>

      <td>
        Listing History Entry - Date Listed\
        *Data type: Date*  

        The date the property was listed for sale or rent, in ISO 8601 format
      </td>

      <td>
        `"2024-06-24T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .removedDate
        ```
      </td>

      <td>
        Listing History Entry - Date Delisted\
        *Data type: Date*  

        The date the property listing was removed or delisted, in ISO 8601 format
      </td>

      <td>
        `"2024-10-01T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        history[YYYY-MM-DD]
        .daysOnMarket
        ```
      </td>

      <td>
        Listing History Entry - Days on Market\
        *Data type: Number*  

        The number of days the property listing has been active
      </td>

      <td>
        `99`
      </td>
    </tr>
  </tbody>
</Table>

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Listing Status Field Values

The following is a list of possible values of the listing `status` response field:

| Listing Status | Description                                                                                                                                                                                                             |
| :------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Active`       | Indicates an active listing, which is currently listed on the market. Returned listing fields will reflect the current listing attributes, such as price, listed date, days on the market, etc.                         |
| `Inactive`     | Indicates an inactive listing, which is not currently listed on the market. Returned listing fields will reflect the last known listing attributes, such as the last known price, listed date, days on the market, etc. |

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Listing Type Field Values

The following is a list of possible values of the listing `listingType` response field:

| Listing Type              | Description                                                                                                                         |
| :------------------------ | :---------------------------------------------------------------------------------------------------------------------------------- |
| `Standard`                | A standard or regular listing, which is not classified as another listing type                                                      |
| `New Construction`        | A listing for a recently constructed property, typically built within the last 12 months                                            |
| `Foreclosure`             | A sale listing that is part of a foreclosure process, typically being sold by a lending institution that foreclosed on the property |
| `Short Sale`              | A sale listing that is part of a short sale process, typically being sold by a financially distressed property owner                |

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>