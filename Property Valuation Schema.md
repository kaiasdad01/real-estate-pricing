Property Valuation Schema

This page contains a data dictionary and a description of all response fields for our property value estimate and rent estimate endpoints (`/avm`).

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Value Estimate Response Fields

The following response fields are specific to the property value estimate endpoint ([`/avm/value`](https://developers.rentcast.io/reference/value-estimate)):

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
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `price`
      </td>

      <td>
        Value Estimate\
        *Data type: Number*  

        The estimated property value, calculated using the RentCast automated valuation model (AVM)
      </td>

      <td>
        `221000`
      </td>
    </tr>

    <tr>
      <td>
        `priceRangeLow`
      </td>

      <td>
        Value Estimate Range - Lower Boundary\
        *Data type: Number*  

        The lower boundary of the property value estimate range, within which we expect the value estimate to fall with 85% confidence
      </td>

      <td>
        `208000`
      </td>
    </tr>

    <tr>
      <td>
        `priceRangeHigh`
      </td>

      <td>
        Value Estimate Range - Upper Boundary\
        *Data type: Number*  

        The upper boundary of the property value estimate range, within which we expect the value estimate to fall with 85% confidence
      </td>

      <td>
        `233000`
      </td>
    </tr>
  </tbody>
</Table>

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Rent Estimate Response Fields

The following response fields are specific to the property rent estimate endpoint ([`/avm/rent/long-term`](https://developers.rentcast.io/reference/rent-estimate-long-term)):

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
        Example Value
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        `rent`
      </td>

      <td>
        Rent Estimate\
        *Data type: Number*  

        The estimated property rent, calculated using the RentCast automated valuation model (AVM)
      </td>

      <td>
        `1670`
      </td>
    </tr>

    <tr>
      <td>
        `rentRangeLow`
      </td>

      <td>
        Rent Estimate Range - Lower Boundary\
        *Data type: Number*  

        The lower boundary of the property rent estimate range, within which we expect the rent estimate to fall with 85% confidence
      </td>

      <td>
        `1630`
      </td>
    </tr>

    <tr>
      <td>
        `rentRangeHigh`
      </td>

      <td>
        Rent Estimate Range - Upper Boundary\
        *Data type: Number*  

        The upper boundary of the property rent estimate range, within which we expect the rent estimate to fall with 85% confidence
      </td>

      <td>
        `1710`
      </td>
    </tr>
  </tbody>
</Table>

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>

## Common Response Fields

The following response fields will be returned by both the property value and rent estimate endpoints:

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
        `latitude`
      </td>

      <td>
        Latitude\
        *Data type: Number*  

        The latitude of the subject property's geographical location
      </td>

      <td>
        `29.475962`
      </td>
    </tr>

    <tr>
      <td>
        `longitude`
      </td>

      <td>
        Longitude\
        *Data type: Number*  

        The longitude of the subject property's geographical location
      </td>

      <td>
        `-98.351442`
      </td>
    </tr>

    <tr>
      <td>
        `comparables`
      </td>

      <td>
        Comparable Properties\
        *Data type: Array*  

        A list of comparable properties that were used to calculate the property value or rent estimate
      </td>

      <td>
        `[ ... ]`
      </td>
    </tr>

    <tr>
      <td>
        `comparables[].id`
      </td>

      <td>
        Comparable - Property Id\
        *Data type: String*  

        A unique RentCast property identifier
      </td>

      <td>
        `"5014-Fern-Lk,-San-Antonio,-TX-78244"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .formattedAddress
        ```
      </td>

      <td>
        Comparable - Formatted Address\
        *Data type: String*  

        The full property address, in the format `Street, Unit, City, State Zip`
      </td>

      <td>
        `"5014 Fern Lk, San Antonio, TX 78244"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .addressLine1
        ```
      </td>

      <td>
        Comparable - Address Line 1\
        *Data type: String*  

        The first line of the property street address
      </td>

      <td>
        `"5014 Fern Lk"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .addressLine2
        ```
      </td>

      <td>
        Comparable - Address Line 2\
        *Data type: String*  

        The second line of the property street address, typically containing the unit or apartment identifier
      </td>

      <td>
        `"Apt 12"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .city
        ```
      </td>

      <td>
        Comparable - Address City\
        *Data type: String*  

        The city of the property address
      </td>

      <td>
        `"San Antonio"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .state
        ```
      </td>

      <td>
        Comparable - Address State\
        *Data type: String*  

        The state of the property address, as a 2-character abbreviation
      </td>

      <td>
        `"TX"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .zipCode
        ```
      </td>

      <td>
        Comparable - Address Zip Code\
        *Data type: String*  

        The 5-digit zip code of the property address
      </td>

      <td>
        `"78244"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .county
        ```
      </td>

      <td>
        Comparable - County\
        *Data type: String*  

        The county in which the property is located
      </td>

      <td>
        `"Bexar"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .latitude
        ```
      </td>

      <td>
        Comparable - Latitude\
        *Data type: Number*  

        The latitude of the property's geographical location
      </td>

      <td>
        `29.471777`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .longitude
        ```
      </td>

      <td>
        Comparable - Longitude\
        *Data type: Number*  

        The longitude of the property's geographical location
      </td>

      <td>
        `-98.350172`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .propertyType
        ```
      </td>

      <td>
        Comparable - Property Type\
        *Data type: String (Enum)*  

        The type of the property. See [explanation of property types](https://developers.rentcast.io/reference/property-types) for possible values
      </td>

      <td>
        `"Single Family"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .bedrooms
        ```
      </td>

      <td>
        Comparable - Number of Bedrooms\
        *Data type: Number*  

        The number of bedrooms in the property, with a value of "0" indicating a studio layout
      </td>

      <td>
        `4`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .bathrooms
        ```
      </td>

      <td>
        Comparable - Number of Bathrooms\
        *Data type: Number*  

        The number of bathrooms in the property
      </td>

      <td>
        `2`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .squareFootage
        ```
      </td>

      <td>
        Comparable - Living Area (Sq.Ft.)\
        *Data type: Number*  

        The total indoor living area of the property, in square feet
      </td>

      <td>
        `1747`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .lotSize
        ```
      </td>

      <td>
        Comparable - Lot Area (Sq.Ft.)\
        *Data type: Number*  

        The total lot size of the property parcel, in square feet
      </td>

      <td>
        `6316`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .yearBuilt
        ```
      </td>

      <td>
        Comparable - Year Built\
        *Data type: Number*  

        The year in which the property was constructed
      </td>

      <td>
        `1986`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .price
        ```
      </td>

      <td>
        Comparable - Listed Price or Rent\
        *Data type: Number*  

        The listed price or rent of the property listing
      </td>

      <td>
        `229900`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .listingType
        ```
      </td>

      <td>
        Comparable - Listing Type\
        *Data type: String (Enum)*  

        The type of the property listing. See [explanation of listing types](https://developers.rentcast.io/reference/property-listings-schema#listing-type-field-values) for possible values
      </td>

      <td>
        `"Standard"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .listedDate
        ```
      </td>

      <td>
        Comparable - Date Listed\
        *Data type: Date*  

        The date the property was most recently listed for sale or rent, in ISO 8601 format
      </td>

      <td>
        `"2024-04-03T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .removedDate
        ```
      </td>

      <td>
        Comparable - Date Delisted\
        *Data type: Date*  

        The date the property listing was most recently removed or delisted, in ISO 8601 format
      </td>

      <td>
        `"2024-05-26T00:00:00.000Z"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .lastSeenDate
        ```
      </td>

      <td>
        Comparable - Date Last Seen\
        *Data type: Date*  

        The date the property listing was most recently seen as active, in ISO 8601 format
      </td>

      <td>
        `"2024-05-25T13:11:55.018Z"`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .daysOnMarket
        ```
      </td>

      <td>
        Comparable - Days on Market\
        *Data type: Number*  

        The number of days the property listing has been active
      </td>

      <td>
        `53`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .distance
        ```
      </td>

      <td>
        Comparable - Distance (Miles)\
        *Data type: Number*  

        The distance between the comparable property and the subject property, in miles
      </td>

      <td>
        `0.2994`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .daysOld
        ```
      </td>

      <td>
        Comparable - Listing Age (Days)\
        *Data type: Number*  

        The number of days since the comparable property listing was last seen as active, indicating the "age" of the comparable property
      </td>

      <td>
        `127`
      </td>
    </tr>

    <tr>
      <td>
        ```
        comparables[]
        .correlation
        ```
      </td>

      <td>
        Comparable - Correlation (%)\
        *Data type: Number*  

        A ratio indicating how similar the comparable property is to the subject property, expressed as a percentage. This ratio ranges from close to "0" (0% similarity) to "1" (100% similarity)
      </td>

      <td>
        `0.9822`
      </td>
    </tr>
  </tbody>
</Table>

<HTMLBlock>{`
&nbsp;
`}</HTMLBlock>